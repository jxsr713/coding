#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import re
import os
import argparse
import getopt
import sys

#######################################################################
# define function
g_dParaKeys = {"f":["func=", "function"],
               "b":["brd=", "board list"],
               "s":["src=", "source file"],
               "d":["dst=", "destine file"],
               "k":["key=", "Search key list"],
               "h":["help", "help function"],
               "v":["ver", "version"]
               }

g_funcType = -1

g_funcLst = ['help',
             'ssd_info', 'scp_brd', 'telnet', 'ssh', #use pexpect function
             'get_ip', 'get_con', 'get_brds', #data from sys_info.tcl
             'pro_brd', 'pro_sch', 'pro_save', 'pro_hdr', 'pro_all' , #data from product web
             'update_csv'                   #update csv files
             ]

g_funcHelp = ['Show command help', 'Show ssd information', 'scp file to a brd',
              'telnet board', 'login board through ssh'
              'Get IP address', "Get console info", "List same type boards",
              "Search product information", "get some info", "save pro info", "print header", "print brds",
              "update csv file from web/tcl"
              ]


g_dataSrc = 0
g_dataFrom = ['csv', 'web']


g_brdLst = []
g_keysLst = []
g_src=""
g_dst=""



def usage():
    """
    The output  configuration file contents.
    Usage: xxxxx.py [-f|--func,[get .....]] [-b|--board,[string]] [-k|--key [keys list] [-h|--help] [-v|--version]

    Description
        -f,--func functions
        -c,--column header string
        -k,--key search string
        -h,--help    Display help information.
        -v,--version  Display version number.
        for example:
            python config.py -d 13
            python config.py -c allow
            python config.py -h
            python config.py -d 13 -c allow
    """
    print("{}     {}".format(paraKeys, paraLst))
    print(g_funcLst)
    print(g_funcHelp)

##########################################################################
def parserOpt():
    global g_funcType, g_funcLst, g_funcHelp, paraKeys, paraLst
    global g_brdLst, g_src, g_dst

    paraKeys = ""
    paraLst = []
    idx = 0
    for pkey, plist in g_dParaKeys.items():
        if idx == 0:
            idx = 1
            paraKeys = pkey
        else:
            paraKeys = paraKeys + ":" + pkey
        paraLst.append(plist[0])

    print("{}  {}\n".format(paraKeys, paraLst))
    try:
        options,args = getopt.getopt(sys.argv[1:], paraKeys, paraLst)
    except getopt.GetoptError as err:
        print(str(err))
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
            if a in g_funcLst:
                g_funcType = g_funcLst.index(a)
            else:
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


def do_qa_func(func, fBase):
    global g_brdLst, g_src, g_dst, g_keysLst
    global g_funcType
    debug = 0
    dRet = {}
    import getQABoardsInfo as qa
    if g_src == "":
        g_src = qa.strTestFile
    cInfo = qa.CQaBrdsInfo(g_src, qa.g_dEorCards, debug)
    dTorList = cInfo.getBrdsFromFile(qa.strTorFile)
    dEorList = cInfo.getBrdsFromFile(qa.strEorFile)
    if func == (fBase + 1):   # get ip
        return
    elif func == (fBase + 2):   # get console
        dSup1 = cInfo.findSUP1(g_brdLst)
        dSup2 = cInfo.findSUP2(g_brdLst)
        dRet.update({"SUP1":dSup1})
        dRet.update({"SUP2":dSup2})
        #print(dRet)
    elif func == (fBase + 3):   # get brds
        dSup1 = cInfo.findBrds4Type(g_keysLst)
        dRet.update({"CARD":dSup1})
    else:
        print("Wrong para!")

    return dRet


def do_prod_func(func,fBase):
    global g_brdLst, g_src, g_dst, g_keysLst
    global g_funcType
    funcBase = fBase
    import getWebInfo as gweb
    if g_src == "":
        g_src = 0
    if g_dst == "":
        g_dst = gweb.g_datafile[0]
    # init class
    cInfo = gweb.CProductInfo(gweb.g_datafile[g_src], g_src)
    nFunc = -1
    cInfo.readAllBrdsInfo()
    if func == (funcBase + 1):   # get board information
        dSearch = cInfo.SearchItem(g_keysLst, 0)
        cInfo.printSearch(dSearch)
    elif func == (funcBase + 2):   # get board some information
        dSearch = cInfo.SearchItem(g_keysLst, 1)
        cInfo.printSearch(dSearch)
    elif func == (funcBase + 3):   # save data to csv file
        print("save information")
        cInfo.writeAllBrds2Csv(g_dst)
    elif func == (funcBase + 4):   # print all boards
        cInfo.printAllBoards()
    elif func == (funcBase + 5):   # print header
        cInfo.printHeader()
    return


def do_pexpect_func(func, fBase):
    global g_brdLst, g_src, g_dst
    import pexpect_telnet as pt
    if func == (fBase + 1):   # get ssd information
        pt.ssd_info_func(g_brdLst)
    elif func == (fBase + 2):   # scp files to a brd
        pt.scp_func(g_brdLst, g_src, g_dst)
    elif func == (fBase + 3):   # login telnet
        dSup = do_qa_func(6, 4)
        dSup1 = dSup['SUP1']
        brdLst = []
        for brd in g_brdLst:
            con = dSup1[brd]
            brdLst.append(con)
        pt.login_brd_func(brdLst, 1)
    elif func == (fBase + 4):   # ssh
        pt.login_brd_func(g_brdLst, 0)
    return

################################################
if __name__ == '__main__':
    parserOpt()
    print("Func:", g_funcType)

    if g_funcType == 0:  # help
        print(usage.__doc__)
        usage()
        exit(0)
    elif g_funcType > 0 and g_funcType <= 4:   # pexpect function
        do_pexpect_func(g_funcType, 0)
    elif g_funcType > 4 and g_funcType <= 7:   # qa function
        do_qa_func(g_funcType, 4)
    elif g_funcType > 7 and g_funcType <= 14:   # get
        do_prod_func(g_funcType, 7)
    else:
        print("No valid function!!!!")
        exit(0)

