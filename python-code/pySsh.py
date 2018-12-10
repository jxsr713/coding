#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import threading

from pexpect import *

def ssh2(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            #           stdin.write("Y")
            #           #简单交互，输入
            #           ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print(o)
                print('%s\tOK\n'%(ip))
        ssh.close()

    except:
        print('%s\tError\n'%(ip))


def scp_file(ip, login, pwd, fileName):
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

# 登录用户名
loginName = 'diag'
# 用户名密码
loginPassword = 'ins123diag'
loginprompt = '[$#>]|[\d]]'

if __name__ == '__main__':
    cmd = ['cal', 'echo hello!']    # 你要执行的命令列表
    username = ""  # 用户名
    passwd = ""    # 密码
    threads = []   # 多线程
    print "Begin......"
    for i in range(1, 254):
        ip = '192.168.1.'+str(i)
        a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        a.start()
