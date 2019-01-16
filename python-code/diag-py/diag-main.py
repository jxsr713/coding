#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import argparse
import getopt
import sys

###############################################################
# define function
###############################################################
#### short_func: long func, description
g_dParaKeys = {"f":["func=", "function"],
               "b":["brd=", "board list"],
               "s":["src=", "source file"],
               "d":["dst=", "destine file"],
               "k":["key=", "Search key list"],
               "h":["help", "help function"],
               "v":["ver", "version"]
               }

g_funcType = -1


g_dataSrc = 0
g_dataFrom = ['csv', 'web']


g_brdLst = []
g_keysLst = []
g_src=""
g_dst=""



def usage(opt=None):
    """
    The output  configuration file contents.
    Usage: xxxxx.py [-f|--func,[get .....]] [-b|--board,[string]] [-k|--key [keys list] [-h|--telp] [-v|--version]
    """

    global g_funcType, g_funcLst, g_funcHelp, paraKeys, paraLst
    print("=== option list ==")
    for pkey, plist in g_dParaKeys.items():
        longName = plist[0].replace("=", "")
        print("    -%s|--%-5s: [%s] "%(pkey, longName, plist[1]))

    print("================ function list =================")
    for key, itm in g_funcLst.items():
        print("\t%-10s: %s"%(key, itm[0]))


##########################################################################
def parserOpt():
    global g_funcType, g_funcLst, g_funcHelp, paraKeys, paraLst
    global g_brdLst, g_src, g_dst

    shortKeys = ""
    longOptLst = []
    idx = 0
    for pkey, plist in g_dParaKeys.items():
        longName = plist[0]
        # if the option have variable, need add ":"
        syb = ""
        if longName.find("=") != -1:
            syb = ":"

        if idx == 0:
            idx = 1
            shortKeys = pkey + syb
        else:

            shortKeys = shortKeys + pkey + syb

        longOptLst.append(plist[0])

    #print("{}  {}\n".format(shortKeys, longOptLst))
    try:
        options,args = getopt.getopt(sys.argv[1:], shortKeys, longOptLst)
    except getopt.GetoptError as err:
        print("[ERROR]!!!!!!!!! ", str(err))
        print(usage.__doc__)
        usage()
        sys.exit(1)

    if not options:
        print(usage.__doc__)
        usage()
        sys.exit(1)

    for opt, a in options:
        print("Get ==:{} {}".format(opt, a))
        if opt in ("-h", "--help"):
            print(usage.__doc__)
            usage()
            exit(0)
        elif opt in ("-f", "--func"):
            print("Get ==:", a)
            if a in g_funcLst.keys():
                g_funcType = a
            else:
                g_funcType = 'help'
                print("invalid function!!!", a)
        elif opt in ("-b", "--board"):
            g_brdLst.append(a)
        elif opt in ("-s", "--src"):
            # 0:all 1:single
            g_src = a
        elif opt in ("-k", "--key"):
            g_keysLst.append(a)
        elif opt in ("-d", "--dst"):
            g_dst = a
        else:
            print("No para: will exe get all boards infor")
    return


def do_qa_func(func):
    global g_brdLst, g_src, g_dst, g_keysLst
    debug = 0
    dRet = {}
    import getQABoardsInfo as qa
    if g_src == "":
        g_src = qa.strTestFile
    cInfo = qa.CQaBrdsInfo(g_src, qa.g_dEorCards, debug)
    if cInfo.loadDataFromJson() == -1:
        dTorList = cInfo.getBrdsFromFile(qa.strTorFile)
        dEorList = cInfo.getBrdsFromFile(qa.strEorFile)
    if func == 0:
        fileName = "/home/weihozha/self-code/coding/python-code/diag-py/qa.json"
        cInfo.saveDataToJson(fileName)
        print("Save qa info to %s"%(fileName))
    elif func == 1:   # get ip
        print("Unsupport !!!!!!")
        return
    elif func == 2:   # get console
        dSup1 = cInfo.findSUP1(g_brdLst)
        dSup2 = cInfo.findSUP2(g_brdLst)
        dRet.update({"SUP1":dSup1})
        dRet.update({"SUP2":dSup2})
        lst = list(dSup1.items()) + list(dSup2.items())
        print("====Get console =====")
        for brd in g_brdLst:
            itm1 = dSup1[brd]
            itm2 = dSup2[brd]
            if itm1:
                strRet = "%-10s: CON1 [%s]"%(brd, itm1)
            if itm2:
                strRet = "%s: CON2 [%s]"%(strRet, itm2)
            print(strRet)

    elif func == 3:   # get TOR brds
        dBrds = cInfo.searchBoards(g_keysLst)
        #dBrds = cInfo.findTorBrds4Type(g_keysLst)

    elif func == 4:   # get EOR brds
        #dBrds = cInfo.findEorBrds4Type(g_keysLst)
        dBrds = cInfo.searchBoards(g_keysLst, None, True)
    else:
        print("Wrong para!")

    return dRet


def do_prod_func(func):
    global g_brdLst, g_src, g_dst, g_keysLst
    import getWebInfo as gweb
    if g_src == "":
        g_src = 0
    if g_dst == "":
        g_dst = gweb.g_datafile[0]
    # init class
    cInfo = gweb.CProductInfo(gweb.g_datafile[g_src], g_src)
    nFunc = -1
    cInfo.readAllBrdsInfo()
    if func == 0:
        print("unsupport the func")
    elif func == 1:   # get board all information
        dSearch = cInfo.SearchItem(g_keysLst, 0)
        cInfo.printSearch(dSearch)
    elif func == 2:   # get board some information
        dSearch = cInfo.SearchItem(g_keysLst, 1)
        cInfo.printSearch(dSearch)
    elif func == 3:   # save data to csv file
        print("save information")
        cInfo.writeAllBrds2Csv(g_dst)
    elif func == 4:   # print all boards
        cInfo.printAllBoards()
    elif func == 5:   # print header
        cInfo.printHeader()
    return


def do_pexpect_func(func):
    global g_brdLst, g_src, g_dst
    import pexpect_telnet as pt
    if func == 1:   # get ssd information
        pt.ssd_info_func(g_brdLst)
    elif func == 2:   # scp files to a brd
        pt.scp_func(g_brdLst, g_src, g_dst)
    elif func == 3:   # login telnet
        dSup = do_qa_func(2)
        print(dSup)
        dSup1 = dSup['SUP1']
        brdLst = []
        for brd in g_brdLst:
            con = dSup1[brd]
            brdLst.append(con)
        print(brdLst)
        pt.login_brd_func(brdLst, 1)
    elif func == 4:   # ssh
        print(g_brdLst)
        pt.login_brd_func(g_brdLst, 0)
    return


def do_r_w_json(fileSrc, strrw, dData):
    import json
    opr = 'r'
    if strrw == 'r':
        opr = 'r'
    elif strrw == 'w':
        opr = 'w'
    else:
        print("wrong operate para")
        return 0

    with open(fileSrc, opr) as f:
        if opr == 'r':
            dData = json.load(f)
        else:
            json.dump(dData, f)
    return 1


#####################################################
# func_key:["description", func_handler, func_para, check para]
#####################################################
g_funcLst = {'backup': ['Save data to json file', do_qa_func, 0, ''],
             'help': ['print command usages', usage, 0, ''],
             'ssd_info': ['Show ssd information', do_pexpect_func, 1, 'b'],
             'scp_brd': ['scp file to a brd', do_pexpect_func, 2, 'sbd'],
             'telnet': ['telnet board', do_pexpect_func, 3, 'b'],
             'ssh': ['ssh board', do_pexpect_func, 4 , 'b'],                   #use pexpect function
             'get_ip': ['Get IP address', do_qa_func, 1, 'b'],
             'get_con': ['Get console info', do_qa_func, 2, 'b'],
             'get_tors': ['List all tor boards with same type boards', do_qa_func, 3, 'k'],       #data from sys_info.tcl
             'get_eors': ['List all EORs with same type boards', do_qa_func, 4, 'k'],       #data from sys_info.tcl
             'pro_brd': ['Search product information according key <hdrname:keys>', do_prod_func, 1, 'k'],
             'pro_sch': ['get product some info specified by -k',do_prod_func, 2, 'k'],
             'pro_save': ['save product table info to cvs file', do_prod_func, 3, ''],
             'pro_hdr': ['print product table header', do_prod_func, 5, ''],
             'pro_all': ['print all brds',do_prod_func, 4 , ''], #data from product web
             'update_csv': ['update csv file from web/tcl', '',0, '']                   #update csv files
             }


def check_paras(strParas):
    global g_brdLst, g_src, g_dst, g_keysLst
    error = 0
    for ch in strParas:
        if ch == 'b': #board list
            if not g_brdLst:
                error = 1
                print("Please input board list: -b <brd>")
        elif ch == 'k':
            if not g_keysLst:
                error = 1
                print("Please input keys list: -k <keys>")
        elif ch == 's':
            if not g_src:
                error = 1
                print("Please input source file: -s <file>")
        elif ch == 'd':
            if not g_src:
                error = 1
                print("Please input destination file: -d <file>")
    return error

################################################
if __name__ == '__main__':
    parserOpt()
    print("Func:", g_funcType)

    funcLst = g_funcLst[g_funcType]

    funcHdl = funcLst[1]
    funcNum = funcLst[2]
    chkLst = funcLst[3]
    print("%s  with %d"%(g_funcType, funcNum))
    if check_paras(chkLst):
        exit(0)
    funcHdl(funcNum)

    exit(0)
    if g_funcType == None:  # backup data
        #do_prod_func(0)
        do_qa_func(0)
    elif g_funcType <= 4:   # pexpect function
        do_pexpect_func(g_funcType - 0)
    elif g_funcType <= 7:   # qa function
        do_qa_func(g_funcType - 4)
    elif g_funcType <= 14:   # get
        do_prod_func(g_funcType - 7)
    else:
        print("No valid function!!!!")
        exit(0)

