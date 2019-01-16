#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import sys
from pexpect import *


def scp_file(ip, fileName, dst):
    # 登录用户名
    login = 'diag'
    # 用户名密码
    pwd = 'ins123diag'
    loginprompt = '[$#>]|[\d]]'

    cmd = 'scp -r ' + fileName + ' ' + login
    cmd = cmd + '@' + ip + ':/' + dst
    print("cmd::", cmd)
    # 注意在events中的后面那个回车符\n
    (command_output, exitstatus) = run(cmd, events={'password': pwd + '\n'},
                                       withexitstatus=1, timeout=200)
    # command_output = run(cmd, events={"[pP]assword": pwd+'\n'})
    print(command_output)
    if exitstatus == 0:
        print("successfully copy file:%s to %s"%(fileName, ip))
    else:
        print("timeout", exitstatus)

    return exitstatus == 0


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc <= 2:
        print("Wrong parameter!!!")
        print("{} <brd_name> <source file> [dest file]".format(sys.argv[0]))
        exit(0)
    brd = sys.argv[1]
    src = sys.argv[2]
    dst = ""
    if argc >= 3:
        dst = sys.argv[3]
    ret = scp_file(brd, src, dst)

    if ret == 1:
        print("Successfully copy!!!")

    exit(0)
