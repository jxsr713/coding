#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import operator

class CQaBrdsInfo(object):
    def __init__(self, infofile, dCardData, debug=0):
        self.fileName = infofile
        self.dBrdsInfo={}
        self.dCardDataBase=dCardData
        self.debug = debug
        self.json = "/home/weihozha/self-code/coding/python-code/diag-py/qa.json"
        return

    def setJson(self, fJson=""):
        self.json = fJson
        if fJson == "":
            self.json = "/home/weihozha/self-code/coding/python-code/diag-py/qa.json"
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
            if debug == 1:
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
            sup1 = resSup1.group(1) + " 20" + resSup1.group(2)
        # check if the ip address is valid
        reExp = re.compile(r'(\d+)\.(\d+)\.(\d+)\.(\d+)')
        reVal = (reExp.search(sup1) is  None)
        if reVal is True:
            if debug == 1:
                print("%s: Invalid SUP1 console ip"%(name))
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
            sup2 = resSup2.group(1) + " 20" + resSup2.group(2)
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
        if debug == 1:
            print("=====Name:", name)
            print(dSubCards)
        # append SUB cards
        dItem.update({'SUB':dSubCards})
        dEORInfo[name] = dItem

        return dEORInfo

    def loadDataFromJson(self, filePath=""):
        import json
        if filePath == "":
            filePath = self.json
        if os.path.exists(filePath) == False:
            print("{} not exist!!".format(filePath))
            return -1
        with open(filePath, 'r') as f:
            try:
                dData = json.load(f)
            except ValueError:
                print('Failed to read %s '%(filePath))
                return -1


        self.dBrdsInfo=dData

        return 0

    def saveDataToJson(self, filePath):
        import json
        dData = self.dBrdsInfo
        with open(filePath, 'w') as f:
            json.dump(dData, f)
        return 0


    '''
    : read system info file to get the information of chassises
    : Name: {sup: "ip port", sup2: ip, apc: ...., psu:... }
    '''
    def getBrdsFromFile(self, filePath):
        debug = self.debug
        fileHandle = open(filePath, 'rb')

        dChassInfo = dict()
        if debug == 1:
            print("@@@@@!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@", filePath)
        try:
            lineNum = 0
            started = 0
            strEOR = ''
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
                    if debug == 1:
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
            #self.printChassisInfo(dChassInfo)
            self.dBrdsInfo.update(dChassInfo)
        finally:
            fileHandle.close()
        return dChassInfo

    def findKeys(self, brdlst, keys, dBrdInfo):
        if dBrdInfo is None:
            dBrdInfo = self.dBrdsInfo

        dRet = {}

        for brd in brdlst:
            if brd in dBrdInfo.keys():
                dInfo = dBrdInfo[brd]
                if keys in dInfo.keys():
                    ret = dInfo[keys]
                    dRet.update({brd:ret})
                else:
                    print("Invalid key string:", keys)
            else:
                print("Invalid board name :", brd)
        print(dRet)
        return dRet

    def findAPC(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "APC", dBrdsInfo)

    def findPSU(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "PSU", dBrdsInfo)

    def findSUP1(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "SUP1", dBrdsInfo)

    def findSUP2(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "SUP2", dBrdsInfo)

    def findIP1(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "IP1", dBrdsInfo,)

    def findIP2(self, brdlst, dBrdsInfo=None):
        return self.findKeys(brdlst, "IP2", dBrdsInfo)

    # search boards with same TYPE
    def findTorBrds4Type(self,  cardType, dBrdsInfo=None ):
        if dBrdsInfo is None:
            dBrdsInfo = self.dBrdsInfo

        brdList = {}
        print(cardType)
        for brd, dInfo in dBrdsInfo.items():
            #print(brd, dInfo, cardType)
            cdTypeStr = dInfo['CARD']
            if not cdTypeStr:
                continue

            if cdTypeStr in cardType:
                if cdTypeStr in brdList.keys():
                    lstVal = brdList[cdTypeStr]
                else:
                    lstVal = []
                lstVal.append(brd)
                brdList.update({cdTypeStr:lstVal})

        print("Board list:", brdList)
        return brdList

    #############################################
    # Get EOR Sub cards from qa folder
    #
    def getEorCardsInfo(self, brd, dData):
        debug = self.debug
        dEor = {'SUP':[], 'LC':[], 'FM':[], 'SC':[]}
        strFile = '/home/ins-diag-qa/sys_cfg/' + brd + '/eor_screening_config_file.tcl.new'
        bExist = os.path.exists(strFile)
        if bExist == False:
            if debug == 1:
                print("%s ! Not exist!".format(strFile))
            return dEor
        #grepCmd = 'egrep  \"^set(.*){([0-9]|\s)+}\" /home/ins-diag-qa/sys_cfg/' + brd + '/eor_screening_config_file.tcl.new'
        grepCmd = 'egrep  \"^set(.*){([0-9]|\s)+}\" ' + strFile
        if debug == 1:
            print(grepCmd)
        matchLst = os.popen(grepCmd).readlines()
        for itm in matchLst:
            if debug == 1:
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
            if debug == 1:
                print("=====:", brdtype)
            for k, l in dData.items():
                if brdtype in l:
                    dEor[k].append({brdtype:match.group(2)})
        if debug == 1:
            print(dEor)
        return dEor


    def findCardType(self, brd, dData):
        debug = self.debug
        cdType = "TOR"
        for k, l in dData.items():
            if brd in l:
                cdType = k
                break
        if debug == 1:
            print("{} : {}".format(brd, cdType))
        return cdType

    def searchBoards(self, brdLst, dInfo = None,  bAnd = False):
        global g_dEorCards
        dCardType = g_dEorCards
        if dInfo is None:
            dInfo = self.dBrdsInfo

        debug = self.debug
        dMatchedCards = {}
        for key, val in dInfo.items():
            bTorFind = 0
            bEorFind = 0
            #print("#####################################")
            for brd in brdLst:
                if debug == 1:
                    print("-------%s------", brd)
                bType = self.findCardType(brd, dCardType)
                if bType == "TOR":
                    card = val['CARD']
                    if operator.eq(card, brd):
                        bTorFind = 1
                        break
                else:
                    bEorFind = 1

                    lCard = val['SUB'][bType]
                    if debug == 1:
                        print("=======", lCard)
                    bGet = 0
                    for ditm in lCard:
                        if debug == 1:
                            print("------", ditm.keys())
                        if brd in ditm.keys():
                            bGet = 1
                            if debug == 1:
                                print(key, "!!!", brd, "===", ditm)
                            break
                    bEorFind = bEorFind & bGet
                    if debug == 1:
                        print("!!!!!!!!!!!!", bEorFind, "===", bGet, "----------------", bAnd)
                    if bAnd:
                        # for and is true, if one board does not matched
                        # then skip the boards
                        if not bEorFind:
                            if debug == 1:
                                print(key, "!--SKIPPPPPPPPP-----!!", brd, "===", ditm)
                            break
                    else:
                        # for And is false
                        # only match one board
                        if bEorFind == 1:
                            break

            if bTorFind | bEorFind:
            #if bEorFind:
                dMatchedCards.update({key:val})
        print("================================================================")
        self.printSearch(brdLst, dMatchedCards)
        return dMatchedCards

    def searchTors(self, brdLst, bAnd = False):
        dBrdsInfo = self.dBrdsInfo
        self.searchBoards(brdLst, dBrdsInfo, bAnd )

    def printSearch(self, brdLst, dSearchResult):
        print("Search boards:{}".format(" ".join(brdLst)))
        print("============================================")
        self.printCards(dSearchResult)

    def printCards(self, dSearchResult=None):
        if dSearchResult is None:
            print("====================All Data===================")
            dData = self.dBrdsInfo
            print(dData)
        else:
            dData = dSearchResult

        idx = 0
        for key, val in dData.items():
            idx = idx +1
            strHeader = "[%03d] %-10s"%(idx, key)
            if val['CARD'] == "":
                brdType = "EOR"
                dInfo = val['SUB']
                if val['SUP2'] == "":
                    sInfo = ""
                else:
                    sInfo = "\n\t\t\tCON2:[{}] ".format(val['SUP2'])

                sInfo = sInfo + "\n\t\t" + "SUB CARDS: "
                for key1, vallst in dInfo.items():
                    sInfo = sInfo + "\n\t\t    " + key1 + ": "
                    for dVal in vallst:
                        for key2, val2 in dVal.items():
                            sInfo = sInfo + key2 + "[" + val2 + "] "
            else:
                brdType = "TOR:{}".format(val['CARD'])
                sInfo = " "

            sSup1 = "CON1:[{}] ".format(val['SUP1'])
            print("{} [{}]: {} {}".format(strHeader, brdType, sSup1, sInfo))
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
strJson = 'qa.json'

g_src = strTestFile

g_dEorCards = {
    'SC':['ALTA'],
    'SUP':['KIRK', 'KSTN', 'ZION'],
    'FM':['MTBK', 'MMTH', 'MTBY', 'MTEVT', 'MTKT', 'MOUN', 'SHWN'],
    'LC':['ABVL','APCH','ARHD','BLAC','BLMT','BLWD','CHCP','CPCK','CSCD',
          'CYNS','CYPR','HONE','load_lc', 'MOEN','MONT','RDLK','RDWD','SEYM',
          'SGLF','SHAS','SIER','SNBDII','SUNR','SVCK','TCMA','WHSL']
}

if __name__ == '__main__':
    cInfo = CQaBrdsInfo(g_src, g_dEorCards, 0)
    tor = cInfo.getBrdsFromFile(g_src)
#    cInfo.printChassisInfo(tor)
    g_src = strEorFile
    eor = cInfo.getBrdsFromFile(g_src)
    brdl = ['RDLK', "ZION"]
    cInfo.searchTors(brdl)
    #cInfo.searchBoards(brdl, eor, g_dEorCards )
    print("================================================")
    print("================================================")
    brdl = ['FOSTERS', "PARIS"]
    cInfo.searchTors(brdl)
    #cInfo.searchBoards(brdl, tor, g_dEorCards)
    print("================================================")
    #cInfo.printChassisInfo(eor)
    #cInfo.printChassisInfo(tor)
    cInfo.getEorCardsInfo("COR4_32", g_dEorCards)
    print("================================================")
    #cInfo.printCards(None)



