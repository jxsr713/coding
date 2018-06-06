#!/usr/bin/python3.3

###############################
#####  IMPORT STATEMENTS  #####
#!usr/bin/env python
##############################

from __future__ import print_function

import re
import os
import importlib

from sys import argv
from sys import path

import imp
try:
    imp.find_module('xlsxwriter')
    XLSX = True
except ImportError:
    XLSX = False
    print("Warning: Module XlsxWriter not found, xlsx output functionality " +
        "disabled. \nFrom the command line, use\n    pip install XlsxWriter\n"+
        "if xlsx output is desired.")
if XLSX:
    import xlsxwriter


# Creates an .xlsx representation of the same table, with polarity
# flips highlighted for readability
def make_xlsx(outputfile, header=True):
    assert(XLSX)
    wb = xlsxwriter.Workbook(outputfile)
    ws = wb.add_worksheet()
    header = wb.add_format({'bold': True})
    header.set_align('center')
    header.set_border(1)
    header.set_bottom(5)
    normal = wb.add_format()
    normal.set_align('center')
    normal.set_border(1)
    flip = wb.add_format()
    flip.set_bg_color('#CCCCCC')
    flip.set_align('center')
    flip.set_border(1)

    normal_q = wb.add_format()
    normal_q.set_align('center')
    normal_q.set_border(1)
    normal_q.set_bottom(5)
    flip_q = wb.add_format()
    flip_q.set_bg_color('#CCCCCC')
    flip_q.set_align('center')
    flip_q.set_border(1)
    flip_q.set_bottom(5)
    r = 0
    c = 0
    widths = [5, 5, 10, 10, 12, 10, 12, 10, 10, 5, 5, 8.43, 8.43, 12]
    ws.write(0, 13, 'LEGEND', header)
    ws.write(1, 13, 'Regular link', normal)
    ws.write(2, 13, 'Polarity flip', flip)
    if header:
        labels = ['port', 'lane', 'RT.L.RX', 'RT.S.TX', 'RX',
            'SWITCH', 'TX', 'RT.S.RX', 'RT.L.TX', 'lane', 'port']
        header.set_bottom(5)
        for label in labels:
            ws.write(r, c, label, header)
            c += 1
        r += 1
        c = 0
    cnt = 10
    for row in range(cnt):
        nextrow = []
        nextrow.append("str(row[0]).zfill(2)")
        nextrow.append("str(row[1]).zfill(2)")
        nextrow.append("row[2]")
        nextrow.append("row[3]")
        nextrow.append("str(row[4]).zfill(2) + row[5]")
        nextrow.append("row[6]")
        nextrow.append("str(row[7]).zfill(2) + row[8]")
        nextrow.append("row[9]")
        nextrow.append("row[10]")
        nextrow.append("str(row[11]).zfill(2)")
        nextrow.append("str(row[12]).zfill(2)")
        for entry in nextrow:
            if r % 4 == 0:
                if '*' in entry:
                    ws.write(r, c, entry[0:-1], flip_q)
                else:
                    ws.write(r, c, entry, normal_q)
            else:
                if '*' in entry:
                    ws.write(r, c, entry[0:-1], flip)
                else:
                    ws.write(r, c, entry, normal)

            c += 1
        r += 1
        c = 0
    for i in range(len(widths)):
        ws.set_column('%c:%c' % (chr(65 + i), chr(65 + i)), widths[i])

    wb.close()

def main():
    board_name = argv[1]
    print(board_name)
    make_xlsx("Test.xls")


if __name__ == "__main__":
    main()
