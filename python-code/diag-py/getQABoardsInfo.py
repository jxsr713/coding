#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import re
import os

class CQaBrdsInfo(object):
    def __init__(self, infofile, dCardData={}, debug=0):
        self.fileName = infofile
        self.dBrdsInfo={}
        self.dCardDataBase=dCardData
        self.debug = debug
        return


    def printChassisInfo(self, dChassis):
        idx = 0
        for key, val in dChassis.items():
            idx = idx +1
            print("[%03d] %-10s"%(idx, key), end='')
            print("===>>>{}".format(val))
            continue
            print("=======Name:%s======="%key)
            print("SUP1:", val["SUP1"], end=" " )
            print("SUP2:", val["SUP2"])
            print("APC:", val["APC"])
            print("PSU:", val["PSU"])
            print("CARD:", val["CARD"])
        return

    '''
    : parser a information string get name, sup1/2 , apc and psu
    : input a string
    : return a dict include information
    : "   PIDMB5 {ts_IP_sup1 "172.31.162.38" ts_line_sup1 "08" ts_IP_sup2 "172.21.159." ts_line_sup2 "05"
    :             apc_port {"172.31.162.52 17 18"} psu_cnt "2" card_cfg "PIPEDREAM"
    :               }"
    '''
    def ParserChassisStr(self, strEOR):
        dDataBase = self.dCardDataBase
        debug = self.debug
        dEORInfo = {}
        dItem = {}
        if debug == 1:
            print("start parser string:", strEOR)
        # regexp for finding chassis name
        regExp = re.compile(r'(\w+) {')
        rstName = regExp.search(strEOR)
        name=""
        if rstName:
            name = rstName.group(1)
            print("=================\nName:", rstName.group(1))
        else:
            return None

        # regexp for finding sup1 condole ip and port
        regExp = re.compile(r'ts_IP_sup1 "([\d|.]+)" ts_line_sup1 "(\d+)"')
        resSup1 = regExp.search(strEOR)
        sup1=""
        if resSup1:
            if debug == 1:
                print("IP:", resSup1.group(1), end='  ')
                print("port:", resSup1.group(2))
            sup1 = resSup1.group(1) + " " + resSup1.group(2)
        # check if the ip address is valid
        reExp = re.compile(r'(\d+)\.(\d+)\.(\d+)\.(\d+)')
        reVal = (reExp.search(sup1) is  None)
        if reVal is True:
            print("Invalid SUP1 console ip\n")
            return None
        dItem["SUP1"] = sup1


        # regexp for finding sup2 condole ip and port
        regExp = re.compile(r'ts_IP_sup2 "([\d|.]+)" ts_line_sup2 "(\d+)"')
        resSup2 = regExp.search(strEOR)
        sup2=""
        if resSup2:
            if debug == 1:
                print("IP2:", resSup2.group(1), end=' ')
                print("port2:", resSup2.group(2))
            sup2 = resSup2.group(1) + " " + resSup2.group(2)
            reExp = re.compile(r'(\d+)\.(\d+)\.(\d+)\.(\d+)')
            reVal = (reExp.search(sup2) is  None)
            if reVal == True:
                sup2 = ""
        dItem["SUP2"] = sup2

        # regexp for finding apc ip and port
        regExp = re.compile(r'apc_port {([\d|.|\s|"]+)}')
        resApc = regExp.search(strEOR)
        apc=""
        if resApc:
            if debug == 1:
                print("APC:", resApc.group(1))
            apc = resApc.group(1)
        dItem["APC"] = apc

        # regexp for finding apc ip and port
        regExp = re.compile(r'psu_cnt "(\d+)"')
        resPsu = regExp.search(strEOR)
        psu=""
        if resPsu:
            if debug == 1:
                print("PSU:", resPsu.group(1))
            psu = resPsu.group(1)
        dItem["PSU"] = psu

        # regexp for finding cfg
        regExp = re.compile(r'card_cfg "(\w+)"')
        resCard = regExp.search(strEOR)
        card=""
        if resCard:
            if debug == 1:
                print("CARD:", resCard.group(1))
            card=resCard.group(1)
        dItem["CARD"] = card

        # create a dict
        # to find sub cards info, just for EOR
        dSubCards = self.getEorCardsInfo(name, dDataBase)
        print("=====Name:", name)
        print(dSubCards)
        # append SUB cards
        dItem.update({'SUB':dSubCards})
        dEORInfo[name] = dItem

        return dEORInfo

    '''
    : read system info file to get the information of chassises
    : Name: {sup: "ip port", sup2: ip, apc: ...., psu:... }
    '''
    def ParserFile(self, filePath):
        debug = self.debug
        fileHandle = open(filePath, 'rb')

        try:
            lineNum = 0
            started = 0
            strEOR = ''
            dChassInfo = dict()
            for line in fileHandle.readlines():
                lineNum = lineNum + 1
                # Fixed error:can't use a string pattern on a bytes-like object
                line = line.decode('utf-8')
    #                result = regex.findall(line)
                # remove '\n' char in start/end of string
                line = line.strip('\n')
                if started == 0:
                    result = re.search(r'set tb_dict', line)
                    if result is None:
                        continue
                    started = 1
                    continue

                result = re.search(r'^}', line)
                if result:
                    print("=== stop parser!!!!")
                    started = 0
                    break

                startParser = 0
                line = line.strip('\\')
                line = line.strip('\t')
    #            print("###", line)
                result = re.search(r'}[\s]*$', line)
                if result:
                    startParser = 1

                strEOR = strEOR + line

                if startParser == 1:
                    if debug == 1:
                        print("-----------------@@@@@@@@@@-------------------")
                        print(strEOR)
                        print("--------------------------------------------")
                    dEORItem = self.ParserChassisStr(strEOR)
                    if not dEORItem  is None:
                        dChassInfo.update(dEORItem)
                        # merge new chassis info into dict
                        if debug == 1:
                            print("######################\n", dEORItem)
                    strEOR = ''
            self.printChassisInfo(dChassInfo)
            self.dBrdsInfo = dChassInfo
            return dChassInfo
        finally:
            fileHandle.close()

    def findKeys(self, dBrdInfo, brd, keys):
        ret = ""
        if brd in dBrdInfo.keys():
            dInfo = dBrdInfo[brd]
            if keys in dInfo.keys():
                ret = dInfo[keys]
            else:
                print("Invalid key string:", keys)
        else:
            print("Invalid board name :", brd)
        return ret

    def findAPC(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "APC")

    def findPSU(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "PSU")

    def findSUP1(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "SUP1")

    def findSUP2(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "SUP2")

    def findIP1(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "IP1")

    def findIP2(self, dBrdsInfo, brd):
        return self.findKeys(dBrdsInfo, brd, "IP2")

    def findBrds4Type(self, dBrdsInfo, brd, cardType):
        brdList = []
        for brd, dInfo in dBrdsInfo.items():
            cdTypeStr = dInfo['CARD']
            if cmp(cdTypeStr.upper(), cardType.upper()) == 0:
                brdList.append([brd, dInfo['SUP1']])
        print("Board list:", brdList)
        return brdList


    def getEorCardsInfo(self, brd, dData):
        dEor = {'sup':[], 'lc':[], 'fm':[], 'sc':[]}
        grepCmd = 'egrep  \"^set(.*){([0-9]|\s)+}\" /home/ins-diag-qa/sys_cfg/' + brd + '/eor_screening_config_file.tcl.new'
        print(grepCmd)
        matchLst = os.popen(grepCmd).readlines()
        for itm in matchLst:
            print(itm)
            match = re.search(r'([A-Z]+)_list {([\d|\s]+)}', itm)
            if match:
                brdtype = match.group(1)
            else:
                match = re.search(r'(load_lc) {([\d|\s]+)}', itm)
                if match:
                    brdtype = match.group(1)
                else:
                    continue
            print("=====:", brdtype)
            for k, l in dData.items():

                if brdtype in l:
                    dEor[k].append({brdtype:match.group(2)})
        print(dEor)
        return dEor


    def findCardType(self, brd, dData):
        cdType = "TOR"
        for k, l in dData.items():
            if brd in l:
                cdType = k
                break
        print("{} : {}".format(brd, cdType))
        return cdType

    def searchBoards(self, brdLst, dInfo, dDataBase):
        dMatchedCards = {}
        for key, val in dInfo.items():
            bfind = 0
            for brd in brdLst:
                bType = self.findCardType(brd, dDataBase)
                if bType == "TOR":
                    card = val['CARD']
                    if cmp(card, brd) == 0:
                        bfind = 1
                        dMatchedCards.update({key:val})
                        break
                else:
                    lCard = val['SUB'][bType]
                    print("=======", lCard)
                    bGet = 0
                    for ditm in lCard:
                        if brd in ditm.keys():
                            bGet = 1
                            break
                    if bGet == 1:
                        bfind = 1
                    else:
                        if bfind == 1:
                            bfind = 0
                            break
            if bfind == 1:
                dMatchedCards.update({key:val})
        self.printSearch(brdLst, dMatchedCards)
        return dMatchedCards


    def printSearch(self, brdLst, dSearchResult):
        print("Search boards:{}".format(" ".join(brdLst)))
        print("============================================")
        idx = 0
        for key, val in dSearchResult.items():
            idx = idx +1
            strHeader = "[%03d] %-10s: "%(idx, key)
            if val['CARD'] == "":
                brdType = "EOR"
                dInfo = val['SUB']
                if val['SUP2'] == "":
                    sInfo = ""
                else:
                    sInfo = "\n\t\tCON2:[{}] ".format(val['SUP2'])

                for key1, vallst in dInfo.items():
                    sInfo = sInfo + "\n\t\t" + key1 + ": "
                    for dVal in vallst:
                        for key2, val2 in dVal.items():
                            sInfo = sInfo + key2 + "[" + val2 + "] "
            else:
                brdType = "TOR:{}".format(val['CARD'])
                sInfo = " "

            sSup1 = " CON1:[{}] ".format(val['SUP1'])
            print("{} ==={} {} {}".format(strHeader, brdType, sSup1, sInfo))
        return





#########################################################
#TOR information
#/home/honjiang/diag_qa/TOR/P_system_info_dev_tor.tcl
#EOR information
#/home/honjiang/diag_qa/EOR/./P_system_info_dev_new_sup.tcl
#IP file: diag-qa-01:/vol/diag/logs/torip_file
#EOR sys information:/home/ins-diag-qa/sys_cfg
#########################################################


strTorFile = "/home/honjiang/diag_qa/TOR/P_system_info_dev_tor.tcl"
strEorFile = "/home/honjiang/diag_qa/EOR/./P_system_info_dev_new_sup.tcl"
strTestFile = "./system_info_tor.tcl"
strEorSys = "/home/ins-diag-qa/sys_cfg/"

g_src = strTestFile

g_dEorCards = {
    'fm':['MTBK', 'MMTH', 'MTBY', 'MTEVT', 'MTKT', 'MOUN', 'SHWN'],
    'sc':['ALTA'],
    'sup':['KIRK', 'KSTN', 'ZION'],
    'lc':['ABVL','APCH','ARHD','BLAC','BLMT','BLWD','CHCP','CPCK','CSCD',
          'CYNS','CYPR','HONE','load_lc', 'MOEN','MONT','RDLK','RDWD','SEYM',
          'SGLF','SHAS','SIER','SNBDII','SUNR','SVCK','TCMA','WHSL']
}

if __name__ == '__main__':
    cInfo = CQaBrdsInfo(g_src, g_dEorCards, 1)
#    tor = cInfo.ParserFile(g_src)
#    cInfo.printChassisInfo(tor)
    g_src = strEorFile
    eor = cInfo.ParserFile(g_src)
    brdl = ['RDLK']
    cInfo.searchBoards(brdl, eor, g_dEorCards)
    #cInfo.printChassisInfo(eor)
    cInfo.printChassisInfo(tor)
    cInfo.getEorCardsInfo("COR4_32", g_dEorCards)




