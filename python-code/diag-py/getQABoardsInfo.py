#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import re
import os

class CQaBrdsInfo(object):
    def __init__(self, infofile, debug=0):
        self.fileName = infofile
        self.dBrdsInfo={}
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

#########################################################
#TOR information
#/home/honjiang/diag_qa/TOR/P_system_info_dev_tor.tcl
#EOR information
#/home/honjiang/diag_qa/EOR/./P_system_info_dev_new_sup.tcl

strTorFile = "/home/honjiang/diag_qa/TOR/P_system_info_dev_tor.tcl"
strEorFile = "/home/honjiang/diag_qa/EOR/./P_system_info_dev_new_sup.tcl"
strTestFile= "./system_info_tor.tcl"

g_src=strTestFile
if __name__ == '__main__':
    cInfo = CQaBrdsInfo(g_src, 1)
    tor = cInfo.ParserFile(g_src)
    cInfo.printChassisInfo(tor)
    g_src = strEorFile
    eor = cInfo.ParserFile(g_src)
    cInfo.printChassisInfo(eor)
    cInfo.printChassisInfo(tor)

