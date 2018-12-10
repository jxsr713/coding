#!/usr/bin/python
# -*-coding:utf-8 -*-

import os
import time

import telnetlib

from subprocess import Popen, PIPE, call

#retcode = os.system("ssh diag@172.31.236.172\n")
#print("retcode is: %s" % retcode);
Host = "172.31.162.38"
finish = "Username:"
#tn = telnetlib.Telnet(Host
tn = telnetlib.Telnet(Host, port=2030, timeout=10 )
time.sleep(2)
result = tn.read_some()
result = tn.read_some()
print(result.decode('ascii'))

#tn.read_until(finish.encode('utf-8'))
#tn.read_until(finish)
tn.write(b'admin\n')
finish = "Password:"
print("===")
tn.write(b'insieme\n')
print("===2")
tn.write(b'ls\n')
finish = "~]#"
print("===3")
tn.write(b'ls\n')
#tn.read_until(finish.encode('utf-8'))

time.sleep(2)
print("===34")

tn.write(b'exit\n')
tmp = tn.read_all()
tn.close()

print(tmp.decode('ascii'))


exit()


fouput = os.popen("ssh diag@172.31.236.172", "w")

fouput.write("1234\n")



