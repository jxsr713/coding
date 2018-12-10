#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


def get_prime(num):
    primelst = []
    cmpcnt = 0
    for ii in range(2 ,int(num)):
        add = 1
        for zz in primelst:
            cmpcnt = cmpcnt + 1
            if ii % zz == 0:
                add = 0
                break
        if add == 1:
            primelst.append(ii)
    cnt = len(primelst)

    print("Get list[{}]:{}".format(cnt, primelst))
    print("Total :{}".format(cmpcnt))

if __name__ == '__main__':
    num = input("Input number:")
    get_prime(num)
