#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import re
import os

def printChassisInfo(dChassis):
    for key, val in dChassis.items():
        print("=======Name:%s======="%key)
        print("SUP1:", val["SUP1"], end=" " )
        print("SUP2:", val["SUP2"])
        print("APC:", val["APC"])
        print("PSU:", val["PSU"])

'''
: parser a information string get name, sup1/2 , apc and psu
: input a string
: return a dict include information
'''
def ParserChassisStr(strEOR):
    dEORInfo = {}
    dItem = {}
#    print("start parser EOR string:", strEOR)
    # regexp for finding chassis name
    regExp = re.compile(r'(\w+) {')
    rstName = regExp.search(strEOR)
    if rstName:
        print("=================\nName:", rstName.group(1))

    # regexp for finding sup1 condole ip and port
    regExp = re.compile(r'ts_IP_sup1 "([\d|.]+)" ts_line_sup1 "(\d+)"')
    resSup1 = regExp.search(strEOR)
    if resSup1:
#        print("IP:", resSup1.group(1), end='  ')
#        print("port:", resSup1.group(2))
        dItem["SUP1"] = resSup1.group(1) + " " + resSup1.group(2)

    # regexp for finding sup2 condole ip and port
    regExp = re.compile(r'ts_IP_sup2 "([\d|.]+)" ts_line_sup2 "(\d+)"')
    resSup2 = regExp.search(strEOR)
    if resSup2:
#        print("IP:", resSup2.group(1), end=' ')
#        print("port:", resSup2.group(2))
        dItem["SUP2"] = resSup2.group(1) + " " + resSup2.group(2)

    # regexp for finding apc ip and port
    regExp = re.compile(r'apc_port {([\d|.|\s|"]+)}')
    resApc = regExp.search(strEOR)
    if resApc:
#        print("APC:", resApc.group(1))
        dItem["APC"] = resApc.group(1)

    # regexp for finding apc ip and port
    regExp = re.compile(r'psu_cnt "(\d+)"')
    resPsu = regExp.search(strEOR)
    if resPsu:
#        print("PSU:", resPsu.group(1))
        dItem["PSU"] = resPsu.group(1)
    # create a dict
    dEORInfo[rstName.group(1)] = dItem

    return dEORInfo

'''
: read system info file to get the information of chassises
: Name: {sup: "ip port", sup2: ip, apc: ...., psu:... }
'''
def ParserFile(filePath):
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
            result = re.search(r'}$', line)
            if result:
                startParser = 1

            strEOR = strEOR + line

            if startParser == 1:
                dEORItem = ParserChassisStr(strEOR)
                # merge new chassis info into dict
                dChassInfo.update(dEORItem)
                strEOR = ''
        printChassisInfo(dChassInfo)

    finally:
        fileHandle.close()

if __name__ == '__main__':
    ParserFile("system_info.tcl")
