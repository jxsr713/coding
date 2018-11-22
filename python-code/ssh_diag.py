#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import pexpect_telnet as pt

# ############## CHECK SSD #############


def get_interact_func(child, dictRtn, ipAddr):
    # loginprompt = ']#'
    loginprompt = '[$#>]'
    cmd = 'lsscsi'
    child.sendline(cmd)
    # 立马匹配 'ls -l'，目的是为了清除刚刚被 echo 回显的命令.
    child.expect('ls -l')
    # 期待提示符出现.
    child.expect(loginprompt)
    # 将 'ls -l' 的命令结果输出.
    print(child.before)
    print("Script recording started. Type to escape from the script shell.")
    # 将 session 子程序的执行权交给用户.
    child.interact()
    print 'Left interactve mode.'
    return


TestAddrLst = ["CT304", "COR16_8", "COR16_1"]


if __name__ == '__main__':
    ipAddrLst = TestAddrLst
    pt.get_ssd_info_v2(ipAddrLst)

    ##########
