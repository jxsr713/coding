#!/usr/bin/python3.3
# -*- coding: utf-8 -*-
import re
import os
import pexpect
import sys
import argparse
import getopt

from pexpect import *
import time


def scp_file_1(ip, login, pwd, fileName):
    cmd = 'scp ' + fileName + ' ' + login
    cmd = cmd + '@' + ip + ':/mnt'
    print("cmd::", cmd)
    # 注意在events中的后面那个回车符\n
    (command_output, exitstatus) = run(cmd, events={'password': pwd + '\n'},
                                       withexitstatus=1)
    # command_output = run(cmd, events={"[pP]assword": pwd+'\n'})
    print(command_output)
    if exitstatus == 0:
        print("successfully copy file:", fileName)
    else:
        print("timeout")

    return exitstatus == 0


def run_cmd(child, cmd, expect):
    child.sendline(cmd)
    # 立马匹配 'ls -l'，目的是为了清除刚刚被 echo 回显的命令.
    child.expect(cmd)
    # 期待提示符出现.
    child.expect(expect)


####################################################################
# telnet
####################################################################
def telnet_or_ssh_login(conType, ipAddress, loginName, loginPassword, debug):
    lstexpect = []
    login = 0
    # 提示符，可能是’ $ ’ , ‘ # ’或’ > ’ 和 dsh下的[xx]
    loginprompt = '[$#>]|[\d]]'
    loginprompt = '~]#'

    lstexpect.append("login")           # index 0
    lstexpect.append("[pP]assword")     # index 1
    lstexpect.append("(?i)Unknown host")    # index 2
    lstexpect.append(loginprompt)
    lstexpect.append("refused")
    lstexpect.append(pexpect.EOF)
    lstexpect.append(pexpect.TIMEOUT)
    # 拼凑 telnet 命令
    if conType == 1:    # telnet
        cmd = 'telnet ' + ipAddress
    else:               # ssh
        cmd = 'ssh ' + loginName + '@' + ipAddress
    if(debug == 1):
        print("Cmd:", cmd)
    # 为 telnet 生成 spawn 类子程序
    child = pexpect.spawn(cmd)
    # 将结果直接输出到屏幕上, 如果python版本是3.3，下面的语句会发生：
    # TypeError: must be str, not bytes
    if(debug == 1):
        child.logfile = sys.stdout

    child.sendline('\n\r')
    # 期待'login'字符串出现，从而接下来可以输入用户名
    while True:
        index = child.expect(lstexpect)
        if(debug == 1):
            print("index:%d" % (index))
        if(index == 0):
            # 匹配'login'字符串成功，输入用户名.
            if(debug == 1):
                print("Match login")
            # child.sendline(loginName)
        elif(index == 1):
            # 期待 "[pP]assword" 出现.
            # 匹配 "[pP]assword" 字符串成功，输入密码.
            child.sendline(loginPassword)
        elif(index == 3):
            login = 1
            break
            # 期待提示符出现.
            # child.expect(loginprompt)
        elif index == 4 or index == 3:
            if(debug == 1):
                print("Connection refused!\n")
            break
        else:
            # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
            if(debug == 1):
                print("telnet login failed, due to TIMEOUT or EOF")
            child.close(True)
            break
    child.buffer = ""
    if login == 1:
        return child

    return 0


def get_hdparm_sec_erase(ipAddr, child):
    # 登录用户名
    loginName = 'diag'
    # 用户名密码
    loginPassword = 'ins123diag'
    loginprompt = '~]#'
    # ipAdadr = "COR16_1"
    debug = 0
    print("\n\n====================={}================".format(ipAddr))
    child = telnet_or_ssh_login(0, ipAddr, loginName, loginPassword, debug)
    if(child == 0):
        print("Failed to login %s" % (ipAddr))
        return -1


def get_hdparm_sec_erase(ipAddr, child):
    loginprompt = '~]#'
    errptrn = re.compile(r"(missing|failed|error)")

    cmd = "hdparm -I /dev/sda"
    invprot = "Checksum"
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
        # print(strBuff)
        pattern = re.compile(r"Model Number:       ([\w|-]*)")
        matched = pattern.search(strBuff)
        if(matched):
            modelNm = matched.group(1)
        else:
            print("Failed to find model")
            return -1

        pattern = re.compile(r"user addressable sectors:(\s*)(\d*)")
        matched = pattern.search(strBuff)
        if(matched):
            lbaCnt = int(matched.group(2))
            NewlbaCnt=lbaCnt/2
        else:
            print("Failed to lba counter")
            return -1
    child.buffer = ""
    print("=========Get {} LBACNT :::: {}=========".format(modelNm, lbaCnt))

    cmd = "hdparm --user-master u --security-set-pass Eins /dev/sda"
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
        # print(strBuff)
    else:
        print("Timeout ")
        return -1
    matched = errptrn.search(strBuff)
    if(matched):
        print(strBuff)
    child.buffer = ""

    # cmd = "hdparm --user-master u --security-set-pass Eins111 /dev/sda"
    cmd = "hdparm --user-master u --security-erase Eins /dev/sda"
    print("Security erase.......")
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1
    matched = errptrn.search(strBuff)
    if(matched):
        print(strBuff)

    cmd = "hdparm -N /dev/sda"
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1
    matched = errptrn.search(strBuff)
    if(matched):
        print("ERROR::::::{}".format(strBuff))

    pttn = re.compile(r"max sectors   = (\d+)/(\d+)")
    matched = pttn.search(strBuff)
    if(matched):
        lbaCnt = int(matched.group(1))
        TotalCnt = int(matched.group(2))
    else:
        print("Faild to get count")
        print(strBuff)
        return -1
    print("{} / {}".format(lbaCnt, TotalCnt))
    NewlbaCnt = TotalCnt/2
    cmd = "hdparm -Np" + str(NewlbaCnt) + " --yes-i-know-what-i-am-doing /dev/sda"
    print(cmd)
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1
    # print(strBuff)
    matched = errptrn.search(strBuff)
    if(matched):
        print("ERROR::::::\n{}\n::::::::::::".format(strBuff))

    cmd = "hdparm -N /dev/sda"
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1

    pttn = re.compile(r"max sectors   = (\d+)/(\d+)")
    matched = pttn.search(strBuff)
    if(matched):
        lbaCnt = int(matched.group(1))
        TotalCnt = int(matched.group(2))
    else:
        print("Faild to get count")
        print(strBuff)
        return -1
    print("{} / {}".format(lbaCnt, TotalCnt))

    ################### retore count #############
    print("========restore orignal setting======")
    time.sleep(10)
    NewlbaCnt = TotalCnt
    # cmd = "hdparm -Np" + str(NewlbaCnt) + " --yes-i-know-what-i-am-doing /dev/sda"
    cmd = "hdparm -N /dev/sda"
    print(cmd)
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1
    # print(strBuff)
    matched = errptrn.search(strBuff)
    if(matched):
        print("ERROR::::::{}".format(strBuff))

    cmd = "hdparm -N /dev/sda"
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1

    pttn = re.compile(r"max sectors   = (\d+)/(\d+)")
    matched = pttn.search(strBuff)
    if(matched):
        lbaCnt = int(matched.group(1))
        TotalCnt = int(matched.group(2))
    else:
        print("Faild to get count")
        print(strBuff)
        return -1
    print("{} / {}".format(lbaCnt, TotalCnt))

    #########################################################
    cmd = ""
    child.sendline(cmd)
    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
    else:
        print("Timeout ")
        return -1
    print(strBuff)

    return 0


def get_msecli_ssd(ipAddr, child):
    # /diag/bin/msecli -L -d -n /dev/sda
    # /diag/bin/msecli -M -o $NEW_MAX_LBA -z -n $PHYDEV
    # /diag/bin/msecli -L -d -n $PHYDEV`
    return

def login_iplist_with_func(ipAddrLst, func, dictRtn, conType):
    # 登录用户名
    loginName = 'diag'
    # 用户名密码
    loginPassword = 'ins123diag'
    failBrd = []
    for ipAddr in ipAddrLst:
        # print("IP:{}".format(ipAddr))
        child = telnet_or_ssh_login(conType, ipAddr, loginName, loginPassword, 0)
        if(child == 0):
            # print("Failed to login %s" % (ipAddr))
            failBrd.append(ipAddr)
            continue

        func(child, dictRtn, ipAddr)
        child.close(True)
    return failBrd

#def check_emmc_device(child, dictRtn):
#    cmd_

############### CHECK SSD #############
def get_ssd_func(child, dictRtn, ipAddr):
    board = ""
    product = ""
    snstr = ""
    debug = 0
    # Get information of boards
    cmd = "echo TP=$INS_CARD_TYPE NUM=$INS_PRODUCT_NUM"
    invprot = ']#'
    child.sendline(cmd)
    index = child.expect([invprot, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before.decode('utf-8')
        if debug == 1:
            print("\n\n======{}!!!!!!!!\n\n".format(strBuff))
        pattern = re.compile(r"TP=(\w+)")
        matched = pattern.search(strBuff)
        board = matched.group(1) if(matched) else ""
        #    board = matched.group(1)
        if debug == 1:
            print("board {} {}".format(board, matched.group(1)))

        pattern = re.compile(r"NUM=([\w|-]+)")
        matched = pattern.search(strBuff)
        product = matched.group(1) if(matched) else ""

    # get information of SSD
    cmd = "/diag/bin/smartctl -i /dev/sda"
    loginprompt = ']#'
    if debug == 1:
        print("\n\nRun cmd:{}".format(cmd))
    child.sendline(cmd)

    index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
    size = 0
    snstr = ""
    if(index == 0):
        strBuff = child.before.decode('utf-8')
        pattern = re.compile(r"User Capacity:.* \[(\d+)")
        matched = pattern.search(strBuff)
        size = matched.group(1) if(matched) else 0
        #    size = matched.group(1)
        # else:
        #    return
        pattern = re.compile(r"Device Model:\s+([\w|-]+)")
        matched = pattern.search(strBuff)
        snstr = matched.group(1) if(matched) else ""
        #    snstr = matched.group(1)
        # else:
        #     return
    flag = ""
    if size != 0:
        if(snstr.find(size) == -1):
            flag = "Size unmatched!!"
    else:
        flag = "No SSD"

    print("%-10s[%-12s %-10s]  SSD:%-25s   SIZE:%d %s" % (ipAddr, board,
                                            product, snstr, int(size), flag))

    # save SSD information into a DICT
    keyname = product + " " + board
    keyname = board
    keys = dictRtn.get(keyname)
    if(keys is None):
       keys = [snstr]
    else:
       keys.append(snstr)
       keys = list(set(keys))
    #keys = [snstr] if keys is None else  keys.append(snstr)
    if flag != "":
        keys.append(flag)

    dictRtn[keyname] = keys


def get_ssd_info_v2(ipAddrLst):
    conType = 0 # 1: telnet others: ssh
    dSSD = {}
    failbrd = []
    failbrd = login_iplist_with_func(ipAddrLst, get_ssd_func, dSSD, conType)

    keylst = sorted(dSSD)
    print("========print SSD info========")
    for dKeys in keylst:
        print("{}:{}".format(dKeys, sorted(dSSD[dKeys])))

    if failbrd:
        print("There are some board failed to ssh {}:".format(failbrd))
        print("Try again!")
        login_iplist_with_func(failbrd, get_ssd_func, dSSD, conType)


    return


def get_ssd_info(ipAddrLst):

    dSSD = {}
    failBrd = []
    # 登录用户名
    loginName = 'diag'
    # 用户名密码
    loginPassword = 'ins123diag'
    loginprompt = '[$#>]|[\d]]'
    for ipAddr in ipAddrLst:
        # print("IP:{}".format(ipAddr))
        child = telnet_or_ssh_login(0, ipAddr, loginName, loginPassword, 0)
        if(child == 0):
            # print("Failed to login %s" % (ipAddr))
            failBrd.append(ipAddr)
            continue

        board = ""
        product = ""
        snstr = ""
        cmd = "inventory"
        invprot = ']#'
        # invprot = "MAKE_QA_HAPPY"
        # print("======{}".format(child.buffer))
        child.sendline(cmd)
        # print("====111111{}\n111111\n".format(child.buffer))
        # timeout = 30
        index = child.expect([invprot, pexpect.EOF, pexpect.TIMEOUT])
        # index = 2
        # print(index)
        if(index == 0):
            strBuff = child.before
            # print("\n\n======{}!!!!!!!!\n\n".format(strBuff))
            pattern = re.compile(r"Card type \(env\) = ([\w|-]*)")
            matched = pattern.search(strBuff)
            if(matched):
                board = matched.group(1)

            pattern = re.compile(r"PRODUCT_NUMBER  : ([\w|-]*)")
            matched = pattern.search(strBuff)
            if(matched):
                product = matched.group(1)

            pattern = re.compile(r"Gbps  Model=([\w|-]*)")
            matched = pattern.search(strBuff)
            if(matched):
                snstr = matched.group(1)
            else:
                continue
        cmd = "/diag/bin/smartctl -i /dev/sda | grep \"User Capacity:\" | awk -F [ '{ print \"SIZE:\" $2 }' "
        # cmd = "/diag/bin/smartctl -i /dev/sda"
        #  cmd = "smartctl  -a /dev/sda"
        loginprompt = ']#'
        # print("\n\nRun cmd:{}".format(cmd))
        child.sendline(cmd)

        index = child.expect([loginprompt, pexpect.EOF, pexpect.TIMEOUT])
        size = 0
        if(index == 0):
            strBuff = child.before
            # print("aaaaaaan{}!!!!!!!!\n\n".format(strBuff))
            pattern = re.compile(r"SIZE:(\d+)")
            matched = pattern.search(strBuff)
            if(matched):
                size = matched.group(1)
            else:
                continue
        flag = ""
        if(snstr.find(size) == -1):
            flag = "Size unmatched!!"

        # print("@@@@@@@@@@\n\n======{}\naaaaaa".format(child.buffer))
        print("{}: {} {}: {} SIZE:{} {}".format(ipAddr, board,
                                                product, snstr, size, flag))

        # save SSD information into a DICT
        keyname = product + " " + board
        keyname = board
        keys = dSSD.get(keyname)
        if(keys is None):
            keys = [snstr]
        else:
            keys.append(snstr)
            keys = list(set(keys))
        dSSD[keyname] = keys

        child.close(True)

    # print("Failed to login:{}".format(failBrd))

    keylst = sorted(dSSD)
    print("========print SSD info========")
    for dKeys in keylst:
        print("{}:{}".format(dKeys, sorted(dSSD[dKeys])))
    return


########################################################################
# program and check the version
########################################################################
def update_bios(child, fileName):
    cmdFnshKey = "bios_cmd: C_T_N"

    cmd = "bios_cmd program 0 /mnt/" + fileName
    print("Run cmd:", cmd)
    child.sendline(cmd)
    index = child.expect(["y/n", pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):     # cmd finished
        print("Get prompt!!!!!!")
    elif index == 2:
        print("ERROR!!: Timeout!")
        return 0
    child.sendline("n")
    index = child.expect([cmdFnshKey, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):     # cmd finished
        print("BIOS Program finished!")
    elif index == 2:
        print("ERROR!!: Timeout!")
        return 0

    # check the version
    cmd = "bios_cmd info"
    child.sendline(cmd)
    index = child.expect([cmdFnshKey, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):     # cmd finished
        print("%s finished!" % (cmd))
    elif index == 2:
        print("ERROR!!: Timeout!")
        return 0
    # get the version information from the output
    strBuff = child.before
    pattern = re.compile(r"(\w*) {} .* BIOS v([\d|\.]*)".format("Version"))
    matchLst = pattern.findall(strBuff)
    for itm in matchLst:
        print("====::::{} == {}".format(itm[0], itm[1]))

    return 1


def update_fpga(child, fileName):
    cmdFnshKey = "prog_util: C_T_N"
    cmd = "prog_util -name IOFPGA -primary -program " + fileName
    print("Run cmd:", cmd)
    index = child.expect([cmdFnshKey, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):     # cmd finished
        print("FPGA Program finished!")
    elif index == 2:
        print("ERROR!!: Timeout!")
        return 0
    print("Need to power cycle board to check the version\n")


def parserArgs():
    parser = argparse.ArgumentParser(description='manual to this script')
    brd_help = "For TOR: the board is the board name, EOR is board type"
    parser.add_argument('--board', type=str, default=None, help=brd_help)
    parser.add_argument('--ip', type=str, default=None, help='board/sup ip ' )
    parser.add_argument('--func', type=str, default='BIOS', help='BIOS, FPGA')
    parser.add_argument('--file', type=str, default=None, help='image file path')
    parser.add_argument('--type', type=str, default='TOR', help='TOR/EOR')
    args = parser.parse_args()
    print(args)

    return parser
    # prinat(args.batch_size)


####################################################################
Sup2AddrLst = [
    "172.31.236.154", "172.31.162.112", "172.31.162.119",
    "172.31.162.215", "172.31.162.168", "172.31.236.217",
    "172.31.236.104", "172.31.162.229", "172.31.236.241",
    "172.31.236.155", "172.31.236.190", "172.31.162.125",
    "172.31.162.160", "172.31.162.156", "172.31.162.232",
    "172.31.162.171", "172.31.236.156", "172.31.236.113",
    "172.31.162.113", "172.31.236.162", "172.31.162.175",
    "172.31.162.220"]

EorAddrLst = ["COR16_1", "COR16_2", "COR16_3", "COR16_4",
              "COR16_5", "COR16_6", "COR16_8", "COR16_9",
              "COR4_26", "COR4_27", "COR4_28", "COR4_30",
              "COR4_31", "COR4_32", "COR4_44", "COR4_50",
              "COR4_53", "COR4_54", "CT13", "CT156",
              "CT157", "CT168", "CT169", "CT170",
              "CT19A", "CT201", "CT202", "CT203",
              "CT204", "CT205", "CT206", "CT207",
              "CT209", "CT300", "CT303", "CT304",
              "CT305", "CT306"]
TorAddrLst = ['ATWP002', 'ATWP004', 'ATWP1', 'ATWP3',
              'ATWP5', 'BANF1', 'BDOG1', 'BDOG2',
              'BDOG3', 'BDTN2', 'BDTN3', 'BDTN4',
              'BDTN5', 'BFST4', 'BFST5', 'BFST7',
              'BFST8', 'BFST9', 'BLVU003', 'BLVU004',
              'BLVU007', 'BLVU5', 'BLVU6', 'BRLN002',
              'BRLN1', 'BRLN1_CRDC', 'BRLN3', 'BRLN4',
              'BRLN5', 'BRLN6', 'BRLN7', 'BRLN8',
              'CAGA004', 'CAGA2', 'CHMX002', 'CHMX004',
              'CHMX005', 'CHMX006', 'CHMX11', 'CHMX7',
              'CHMX8', 'CHMX9', 'CHMX_MDVT', 'COLA1',
              'COLA2', 'COLA21', 'COLA22', 'COLA23',
              'COOR003', 'COOR004', 'COOR2', 'COR001',
              'COR2', 'COR3', 'COR4', 'COR5',
              'CT700', 'DEVL005', 'DEVL1', 'DEVL2',
              'DEVL3', 'DEVL4', 'DEVL444', 'DEVL5',
              'DEVL7', 'DEVL8', 'DEVLN', 'DPBK10',
              'DPBK4', 'DPBK5', 'DPBK6', 'DPBK7',
              'DPBK8', 'DPLK1', 'DPLK2', 'DPLK4',
              'DPLK5', 'DPLK6', 'DPLK8', 'ELYS1',
              'ELYS2', 'FOST10', 'FOST11', 'FOST1_CRDC',
              'FOST4', 'FOST5', 'FOST6', 'FOST7',
              'FOST8', 'FOST9', 'HAGN2', 'HAGN3',
              'HAGN4', 'HAGN7', 'HAGN8', 'HAGN9',
              'HAKM1', 'HAKM2', 'HVSU004', 'HVSU005',
              'HVSU006', 'HVSU007', 'HVSU1', 'HVSU3',
              'HVSUB1', 'HVSU_CR002', 'HVSU_OE1', 'HVSU_XR1',
              'KRIEK1', 'KSGT1', 'KSGT2', 'KSGT3',
              'KSGT4', 'KSGT5', 'KSGT6', 'KSGT7',
              'KSGT8', 'LIHM1', 'LP_M1', 'LP_M2',
              'LP_M3', 'LP_M4', 'LP_M5', 'MABK2',
              'MABK4', 'MABK5', 'MABK6', 'MABK7',
              'MABK8', 'MSHT002', 'MSHT1', 'MSHT5',
              'NAGN_M4', 'NEPT1', 'NEPTCR2', 'NGF1',
              'NGF2', 'NGF3', 'NOOK005', 'NOOK007',
              'NOOK100', 'NOOK102', 'NOOK200', 'NOOK201',
              'NOOK21_CRDC', 'NOOK4', 'NOOK6', 'NOOK8',
              'OSLO002', 'OSLO4', 'OSLO5', 'OSLO_PLUS1',
              'OSLO_TEST1', 'OSLO_TEST2', 'PARIS002', 'PARIS1',
              'PARIS1_CRDC', 'PARIS3', 'PARIS4', 'PARIS5',
              'PARIS6', 'PARIS7', 'PARIS8', 'PERO1',
              'PIDM1', 'PIDM2', 'PIDM3', 'PIDM4',
              'PIWK', 'QI2CR1', 'QI2CR2', 'QI2CR3',
              'QI2XL1', 'QI2XL2', 'QKZK1', 'QZ2CR1',
              'QZ2XL3', 'RDCT1', 'RDCT2', 'RDCT3',
              'RDCT4', 'RED2', 'RED3', 'RED4',
              'RED5', 'SAPO002', 'SAPO004', 'SAPO1',
              'SAPO_PLUS1', 'SAPO_PLUS2', 'SAPO_PLUS3', 'SAPO_PLUS4',
              'SARA002', 'SARA1', 'SARA3', 'SCSW10',
              'SCSW11', 'SCSW12', 'SCSW8', 'SCSW9',
              'SEOUL005', 'SEOUL10', 'SEOUL11', 'SEOUL12',
              'SEOUL13', 'SEOUL14', 'SEOUL15', 'SEOUL16',
              'SEOUL17', 'SEOUL18', 'SEOUL2', 'SEOUL8',
              'SEOUL9', 'SHUG1', 'SHUG10', 'SHUG11',
              'SHUG12', 'SHUG13', 'SHUG14', 'SHUG2',
              'SHUG3', 'SHUG4', 'SHUG5', 'SHUG6',
              'SHUG7', 'SHUG8', 'SHUG9', 'SLC1',
              'SLC2', 'SLKE11', 'SLKE12', 'SLKE8',
              'SMPN1', 'SMPN10', 'SMPN11', 'SMPN12',
              'SMPN4', 'SMPN7', 'SMPN8', 'SMPN9',
              'SMTZ006', 'SMTZ10', 'SMTZ5', 'SMTZ7',
              'SMTZ8', 'SMTZ9', 'SOCHI004', 'SOCHI1',
              'SOCHI2', 'SOCHI_M1', 'SOCHI_M2', 'SOCHI_M3',
              'SPUP2', 'STHM002', 'STHM003', 'STHM004',
              'STHM1', 'SVAL002', 'SVAL1', 'SVAL3',
              'TOR3', 'TOR5', 'TTLY10', 'TTLY11',
              'TTLY12', 'TTLY9', 'TURIN1', 'TURIN2',
              'TURIN3', 'TURIN4', 'UTPS1', 'UTPS2',
              'VINA3', 'VINA4', 'VINA5', 'VINA6',
              'WLKE1', 'WLKE10', 'WLKE2', 'WLKE4',
              'WLKE5', 'WLKE6', 'WLKE7']

TestAddrLst = ["CT304", "COR16_8","COR16_1"]



#######################################################################
# define function
g_funcType = -1
rstOpt = 0

g_funcLst = ['help', 'ssd_info', 'scp_brd' , 'telnet', 'ssh']
g_funcHelp = ['Show command help',
              'Show ssd information',
              'scp file to a brd',
              'telnet board',
              'ssh brd'
              ]

paraKeys = "f:b:s:d:hv"
paraLst =["func=", "board", "src=", "dst=", "help", "version"]

g_dataSrc = 0
g_dataFrom = ['csv', 'web']


g_brdLst = []
g_src=""
g_dst=""



def usage():
    """
    The output  configuration file contents.
    Usage: xxxxx.py [-f|--func,[get .....]] [-c|--column,[string]] [-h|--help] [-v|--version]
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

    try:
        options,args = getopt.getopt(sys.argv[1:], paraKeys,  paraLst)
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
        print("Get ==:", opt)
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
        elif opt in ("-d", "--dst"):
            g_dst = a
        else:
            print("No para: will exe get all boards infor")
    return

############################################################################
def ssd_info_func(brdlst):
    brdcnt = len(brdlst)
    lst = brdlst
    if brdcnt == 1:
        argv1 = brdlst[0]
        if argv1 == "all-tor":
            lst = TorAddrLst
        elif argv1 == "all-eor":
            print("EOR")
            lst = EorAddrLst
        elif argv1 == "all-sup2":
            lst = Sup2AddrLst
        elif argv1 == "test":
            lst = TestAddrLst
    print(lst)
    get_ssd_info_v2(lst)
    return

def scp_func(brdlst, src, dst):
    sys.path.insert(0, './')
    from scp_image import scp_file
    for brd in brdlst:
        ret = scp_file(brd, src, dst)
        if ret == 1:
            print("Successfully copy!!!")
    return

############### login boards #############
def login_func(child, para1, para2):
    # first print board information
    cmd = "echo TP=$INS_CARD_TYPE NUM=$INS_PRODUCT_NUM"
    invprot = ']#'
    child.sendline(cmd)
    index = child.expect([invprot, pexpect.EOF, pexpect.TIMEOUT])
    if(index == 0):
        strBuff = child.before
        print(strBuff)
    child.interact()
    return

def login_brd_func(brdlst, conType):
    # conType = 0 # 1: telnet others: ssh
    dict1 = {}
    failbrd = []
    failbrd = login_iplist_with_func(brdlst, login_func, dict1, conType)

################################################
if __name__ == '__main__':
    parserOpt()
    print("Func:", g_funcType)

    if g_funcType == 0:  # help
        print(usage.__doc__)
        usage()
    elif g_funcType == 1:   # get ssd information
        ssd_info_func(g_brdLst)
    elif g_funcType == 2:   # scp files to a brd
        scp_func(g_brdLst, g_src, g_dst)
    elif g_funcType == 3:   # login telnet
        login_brd_func(g_brdLst, 1)
    elif g_funcType == 4:   # ssh
        login_brd_func(g_brdLst, 0)
    else:
        print("No valid function!!!!")
        exit(0)
    '''

    if len(sys.argv) >= 1:
        ipAddrLst = TestAddrLst
        if len(sys.argv) >= 2:
            argv1 = sys.argv[1]
            print("=====", argv1)
            if argv1 == "all-tor":
                ipAddrLst = TorAddrLst
            elif argv1 == "all-eor":
                print("EOR")
                ipAddrLst = EorAddrLst
            elif argv1 == "all-sup2":
                ipAddrLst = Sup2AddrLst
            elif argv1 == "test":
                ipAddrLst = TestAddrLst
            else:
                ipAddrLst = [ sys.argv[1] ]

        else:
            print("Use default ip list: {}".format(TestAddrLst))

        # aget_hdparm_sec_erase(ipAddr)
        get_ssd_info_v2(ipAddrLst)

    else:
        print("Wrong paramet")

    exit(0)

    argsParser = parserArgs()
    if len(sys.argv) == 1:
        argsParser.print_help()
        exit(0)

    args = argsParser.parse_args()

    g_func = args.func
    g_type = args.type
    g_ip = args.ip
    g_file = args.file
    g_board = args.board
    g_connect = 0
    if g_file is None:
        print("Must input <--file>\n")
        argsParser.print_help()
        exit(0)
    if(g_type != 'TOR' and g_type != 'EOR'):
        print("Wrong <type>: ", g_type)
        argsParser.print_help()
        exit(0)

    # if EOR: board use as sup1's ip, we need copy imagefile to board
    if g_type == 'TOR':
        if g_board is None and g_ip is None:
            print("====Please input <board> or <ip> parameter==== ")
            argsParser.print_help()
            exit(0)
        elif g_board is None:
            ipAddress = g_ip
        else:
            ipAddress = g_board

    g_connect = 2   # ssh login
    debug = 1
    # 即将 telnet 所要登录的远程主机的域名
    # ipAddress = '172.31.236.42 2020'    # FOST9
    # ipAddress = '172.31.236.42 2021'    # FOST9
    # ip = "172.31.162.103"
    # ipAddress = "172.31.162.103"

    # 登录用户名
    loginName = 'diag'
    # 用户名密码
    loginPassword = 'ins123diag'
    loginprompt = '[$#>]|[\d]]'

    # ret = scp_file(ip, loginName, loginPassword, './valid')
    # if(ret is False):
    #    exit()


    child = telnet_or_ssh_login(g_connect, ipAddress, loginName, loginPassword, debug)
    # child = ssh_login(2, ipAddress, loginName, loginPassword)
    if child == 0:
        exit(0)

    child.sendline('ls /mnt -l')
    # 立马匹配 'ls -l'，目的是为了清除刚刚被 echo 回显的命令.
    child.expect('ls /mnt -l')
    # 期待提示符出现.
    child.expect(loginprompt)


    # run_cmd(child, "ls / -l\n", loginprompt)
    update_bios(child, './valid')

    child.close(True)
    print("OVER")
    '''

