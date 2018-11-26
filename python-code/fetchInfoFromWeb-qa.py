#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys
import os
import re
import getopt


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find
# https://www.jianshu.com/p/520749be7377
# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# http://uule.iteye.com/blog/2370372

# just read the html test, no js
def readHtml(url):
    res = urllib.request.urlopen(url)
    html = res.read().decode('utf-8')
    print(html)

def readHtmlWithJs(url):
    pass


'''
include 22 fields:   FullName,LaunchDate,ShortName,Base,MPA,SFP,QSFP,10GBASET,CFP,InHouseAsic,CommercialAsic,CPUType,Prompt,PSUNumber,SSDEUSB,ProductNumber,MUX,Retimer,Memory,NIC,Slot,BootImage,EndOfLife
[<table class="tablesorter" id="table">
<thead id="thead"><tr><th class="header">FullName</th><th class="header">LaunchDate</th><th class="header">ShortName</th><th class="header">Base</th><th class="header">MPA</th><th class="header">SFP</th><th class="header">QSFP</th><th class="header">10GBASET</th><th class="header">CFP</th><th class="header">InHouseAsic</th><th class="header">CommercialAsic</th><th class="header">CPUType</th><th cl
ass="header">Prompt</th><th class="header">PSUNumber</th><th class="header">SSDEUSB</th><th class="header">ProductNumber</th><th class="header">MUX</th><th class="header">Retimer</th><th class="header">Memory</th><th class="header">NIC</th><th class="header">Slot</th><th class="header">BootImage</th><th class="header">EndOfLife</th></tr></thead>
<tbody id="tbody">
<tr><td>ANTWERP</td><td>01/01/2016</td><td>ATWP</td><td>Y</td><td>N</td><td>16</td><td>18(TD2)+6(DONNER)</td><td>N/A</td><td>N/A</td><td>TIB x 1  DONNER x 1</td><td>TD2 x 1</td><td>UCS-FI-6332-16UP</td><td>ATWP</td><td>2</td><td>SSD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>diag-sup-x86_64</td><td>N/A</td></tr><tr><td>BODDINGTONS</td><td>09/1
9/2017</td><td>BDTN</td><td>Y</td><td>N</td><td>48</td><td>6x40/100G</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Tofino</td><td>CHIMAY</td><td>BDTN</td><td>2</td><td>SSD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>diag-tor2-x86_64</td><td>N/A</td></tr><tr><td>Bifrost</td><td>02/23/2017</td><td>BFST</td><td>Y</td><td>N</td><td>48</td><td>6x100G</td><td>N/A</td><t
d>N/A</td><td>N/A</td><td>Jericho+</td><td>BifrostCPU</td><td>BFST</td><td>2</td><td>SSD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>diag-tor2-x86_64</td><td>N/A</td></tr>
<tr><td>BELLEVUE</td><td>01/01/2016</td><td>BLVU</td><td>Y</td><td>N</td><td>3</td><td>56(40G)+8(100G)</td><td>N/A</td><td>N/A</td><td>LACROSS x 1</td><td>N/A</td><td>N9K-C92304QC</td><td>BLVU</td><td>2</td><td>SSD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>diag-sup-x86_64</td><td>N/A</td></tr><tr><td>Berlin</td><td>01/01/2016</td><td>BRLN</td><td>Y</td>
<td>N</td><td>1</td><td>6</td><td>48</td><td>1</td><td>TD2+ x1</td><td>N/A</td><td>N3K-C31108TC-V</td><td>BRLN</td><td>2</td><td>SSD</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>diag-sup-x86_64</td><td>N/A</td></tr>
<tr><td>CALGARY</td><td>01/01/2016</td><td>CAGA</td><td>Y</td><td>N</td><td>N/A</td><td>32</td><td>N/A</td><td>N/A</td><td>DONNER x 1</td><td>TD2 x 1<
'''
class CProductInfo(object):
    # def setUp(self):
    def __init__(self, url):
        print("====init====")
        self.driver = webdriver.PhantomJS(executable_path="/usr/bin/phantomjs")
        self.url = url
        self.driver.get(url)
        self.boards = {}
        self.header = {}

    '''
    found the match board according to the image key words
    return the matched boards lista
    first divs is the fullname header
    2nd dive is the all boards name
    3rd div is the colums name
    '''

    '''
    3rd div data format:(col header)
    <th class="header"><span>LaunchDate</span><div class="fht-cell" style="width: 96px;"></div></th>
    <th class="header"><span>ShortName</span><div class="fht-cell" style="width: 116px;"></div></th>
    '''
    def GetColHeader(self, data):
        dictDt = self.header
        lstHd = []
        lsts = data.findAll("span")

        for itm in lsts :
            strItm = str(itm).replace("<span>", "").replace("</span>", "").strip()
            # print(strItm)
            lstHd.append(strItm)
        dictDt["HEADER"] = lstHd
        print(dictDt["HEADER"])
        print("============================================================")

        return

    def GetAllBoardName(self, data):
        dictDt = self.boards
        lstHd = []
        regExp = re.compile(r'>(\w+)<')
        for itm in data :
            lsts = itm.findAll("td")
            rstName = regExp.search(str(lsts))
            if rstName:
                name = rstName.group(1)
                dictDt[name] = None
                #print("=======Name:", rstName.group(1))
        #print(dictDt)
        #print("=================")

    '''
    parser all string
    '''
    def findBoards(self):

        driver = self.driver
        print("==findBoards===")
        #print driver
        #return
        # need to wait enough time to get content from wed
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        divs = soup.findAll("table", {"class": "tablesorter"})
        idx = 0
        for div in divs:
            idx = idx + 1
            rows = div.findAll('tr')

            if idx == 3:
                #print("===>>>>>", div)
                #print("========<<<<<rows:", rows)
                self.GetColHeader(rows[0])
                continue
            elif idx == 2:
                self.GetAllBoardName(rows)
                continue
            elif idx == 1:
                continue
            else:
                self.GetAllData(rows)

    def GetAllData(self, data):
        dictDt = self.boards
        print("=======================boards=======================")
        idx = 0
        #regExp = re.compile(r'>([\w|\/|-]+)<')
        regExp = re.compile(r'>([^\s]+)<')
        for row in data :
            idx = idx + 1
            lstItem = []
            #continue
            lst = row.findAll('td')
            col = 0
            name = None
            #if idx <= 3:
            #    print(lst)
            if len(lst) == 0:
                continue
            for itm in lst:
                rstStr = regExp.search(str(itm))
                col = col + 1
                rst = None
                if rstStr:
                    rst = rstStr.group(1)

                if col == 1:
                    name = rst
                lstItem.append(rst)

            dictDt[name] = lstItem
            #print("=======Name:", dictDt[name])
        #self.printBoards(dictDt)

        return

    def SearchItem(self, header, cmpkey):
        keys = header + ":" + cmpkey
        dValue = {}
        itmlst = []
        lsthdr = self.header["HEADER"]

        if header not in lsthdr:
            print("wrong column:", header)
            print(lsthdr)
            return dValue

        brds = self.boards
        idx = lsthdr.index(header)
        print("Get index:", idx)
        for brd in brds:
            val = brds[brd]
            itmstr = str(val[idx])

            #print(brd)
            #print(itmstr)
            if itmstr.upper().find(cmpkey.upper()) >= 0:
                if idx == 0:    # show boards all information
                    strval = [itmstr, val[0:]]
                else:           # just show board's column information
                    strval = [val[0] , itmstr]
                itmlst.append(strval)

        dValue[keys] = itmlst
        #self.printBoards(dValue)

        return dValue





                # print("Lenght:", leng)
            # skip the header of table

   #  def Balalalala():
   #     if idx == 3:
   #         print("===row:", row)
   #         print("===lst:", lst)
   #         print("=====================$$$$$$$$$$$$==============")
   #     #if len(lst) <= 21:
   #     #    continue
   #     '''
   #     idx = int(idx) + 1
   #     # print("==>>>>", row)
   #     if idx == 5:
   #         print(row)
   #         print(row.findAll('td'))
   #     '''

   #     # find the image name
   #     img = str(lst[21])
   #     if img.find(imgKey) > 0:
   #         # print(img)
   #         # print(lst[9])

   #         # skip boards without asic
   #         asic = str(lst[9]).replace("<td>", "").replace("</td>", "").strip()
   #         if asic.find('N/A') != -1:
   #             asic = str(lst[10]).replace("<td>", "").replace("</td>", "").strip()
   #             if asic.find('N/A') != -1:
   #                 continue
   #         str1 = str(lst[0]).replace("<td>", "").replace("</td>", "").strip()
   #         fnt = str1.find(">")
   #         fnt = fnt + 1
   #         name = str1[fnt:]
   #         lstItem.append(name.strip())

   #         pos = asic.find('x')
   #         if pos != -1:
   #             asic = asic[:pos].strip()
   #         lstItem.append(asic)

   #     #    lstItem.append(img.replace("<td>", "").replace("</td>", "").strip())
   #     #    print("!!%-12s %-20s"%(name,asic))
   #     #    # print(lstItem)

   #         tds.append(lstItem)
   #     return tds

    def printAllBoards(self):
        brd_dict = self.boards
        hdr_dict = self.header
        print(hdr_dict["HEADER"])
        print("============================All Boards=========================")
        for brd_itm in brd_dict:
            val = brd_dict[brd_itm]
            #print(val)
            print("%-20s"%(val[0]), end='')
            print("{}".format(val[1:]))
            #print("")

    def printSearch(self, dList):
        brd_dict = dList
        for brd_itm in brd_dict:
            print("=========%s========"%(brd_itm))
            vallst = brd_dict[brd_itm]
            for itm in vallst:
                #print(val)
                print("%-20s"%(itm[0]), end='')
                print("{}".format(itm[1:]))
            #print("")

import xlrd
class CGetDataFromExcel(object):
    def __init__(self, file):
        self.file = ""
        self.data = []
        if os.path.isfile(file):
            self.file = file

    def parserByRow(self, brd):
        sht_name_lst = ["EOR_CMD", "TOR_COMM_CMD", "TOR_CMD"]
        if len(self.file) == 0:
            print("File %s noexist"%(self.file))
            return -1;
        file_name = self.file
        data = self.data
#        try:
        xls = xlrd.open_workbook(file_name)
        print("open", file_name)
        for sht_name in sht_name_lst:
            print("open", sht_name)
            sht = xls.sheet_by_name(sht_name)
            rows = sht.nrows
            cols = sht.ncols
            print("[r:{} c:{}]".format(rows, cols))
            row_vals = sht.row_values(0)
            #print("sheet:{} =={}".format(sht_name, row_vals))

            #idx = row_vals.find(brd)
            #print("idx:", idx)
            for cc in range(cols):
                brd_str = sht.cell_value(0, cc)
                fnd = brd_str.find(brd)
                if fnd != -1:
                    print("Matched cell[%d %d]:%s"%(0, cc, brd_str))
                    for rr in range(1,rows):
                        cell_str =  sht.cell_value(rr, cc)
                        if len(cell_str.strip()) != 0:
                            val = sht.cell_value(rr, 0)
                            itm_lst = [brd_str, sht_name, val, cell_str]
                            data.append(itm_lst)
                            print(itm_lst)

        return data


    def parserByCol(self, brd):
        sht_name_lst = ["EOR_CMD", "TOR_COMM_CMD", "TOR_CMD"]
        if len(self.file) == 0:
            print("File %s noexist"%(self.file))
            return -1;
        file_name = self.file
        data = self.data
#        try:
        xls = xlrd.open_workbook(file_name)
        print("open", file_name)
        for sht_name in sht_name_lst:
            print("open", sht_name)
            sht = xls.sheet_by_name(sht_name)
            rows = sht.nrows
            cols = sht.ncols
            print("[r:{} c:{}]".format(rows, cols))
            #row_vals = sht.row_values(0)
            #print("sheet:{} =={}".format(sht_name, row_vals))

            #idx = row_vals.find(brd)
            #print("idx:", idx)
            for rr in range(rows):
                brd_str = sht.cell_value(rr, 0)
                fnd = brd_str.find(brd)
                if fnd != -1:
                    print("Matched cell[%d %d]:%s"%(rr, 0, brd_str))
                    for cc in range(1,cols):
                        cell_str =  sht.cell_value(rr, cc)
                        if len(cell_str.strip()) != 0:
                            chas = sht.cell_value(0, cc)
                            itm_lst = [chas + ":" + brd, sht_name, brd_str, cell_str]
                            data.append(itm_lst)
                            print(itm_lst)

        return data

            #if sht_name.find
#        except Exception:
#            print("open %s error: error is %s"%(file_name, "eror"))
#            return -1

def getDataFromExl_main(brd_lst):
    path = "./cli-command.xlsx"
    c = CGetDataFromExcel(path)

    for brd in brd_lst:
        data = c.parserByRow(brd)
        data = c.parserByCol(brd)

    return data


# 还可以进一步实现在界面中去选着下拉框type的中的lc/fm等，来显示对应类型的board，实现与网页交互
def test_main():
    url = r'http://172.31.236.9/html/webtools/prodinfotbl.htm'
    driver = webdriver.PhantomJS(executable_path="C:\\Users\\weihozha\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    idx = 1
    tds = []

def getInfoFromWeb_main(url, keys):
    c = CProductInfo(url)
    c.findBoards()
    c.printAllBoards()
    #dRst = c.SearchItem("BootImage",keys)
    #c.printSearch(dRst)
    dRst = c.SearchItem("InHouseAsic","SUG")
    c.printSearch(dRst)

def SaveData(file_name, data):
    fd = open(file_name, 'w+')
    fd.write("=====================\n")
    for itm in data:
        str1 = u"%-20s [%-15s] [%-40s] \t[%s]\n"%(itm[0], itm[1], itm[2], itm[3])
        print("%s"%(str1))
        fd.write(str1)
    fd.write("*********************\n")
    fd.close()


def getDataFromExl(url):
    log = "C:\\个人文档\\python-working\\cli_output.txt"

    brd_lst = ["FOST", "PARIS", "BRLN", "REDLAKE", "BLUEWOOD", "SPUP", "MTBAKER"]
    data = getDataFromExl_main(brd_lst)
    SaveData(log, data)


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

funcType = -1
headerStr = "FullName"
keyStr = ""

def parserOpt():
    global funcType, headerStr, keyStr
    funcType = 0
    print("OPT===")
    try:
        options,args = getopt.getopt(sys.argv[1:], "f:c:k:hv", ["func=", "column=", "key=", "help", "version"])
    except getopt.GetoptError as err:
        print(str(err))
        print(usage.__doc__)
        sys.exit(1)
    if not options:
        print(usage.__doc__)
        sys.exit(1)

    for opt, a in options:
        print("Get ==:", opt)
        if opt in ("-h", "--help"):
            print(usage.__doc__)
        elif opt in ("-f", "--func"):
            print("Get ==:", a)
            if a in ("getweb"):
                funcType = 1
            elif a in ("sch"):
                funcType = 2
            elif a in ("web"):
                funcType = 3
            elif a in ("getfile"):
                funcType = 4
            elif a in ("write"):
                funcType = 5
            else:
                print("invalid function!!!", a)
        elif opt in ("-c", "--colum"):
            headerStr = a
        elif opt in ("-k", "--key"):
            keyStr = a
        else:
            print("No para: will exe get all boards infor")




if __name__ == "__main__":

    #cardKey = 'lc'
    url = r'http://172.31.236.9/html/webtools/prodinfotbl.htm'
    #argc = len(sys.argv)
    #getInfoFromWeb_main(url, cardKey)


    parserOpt()
#    cInfo = CProductInfo(url)
#    dProdInfo = cInfo.findBoards()
    print("Func:", funcType)
    if funcType == 1:
        cInfo = CProductInfo(url)
        dProdInfo = cInfo.findBoards()
        cInfo.printAllBoards()
    elif funcType == 2:
        cInfo = CProductInfo(url)
        dProdInfo = cInfo.findBoards()
        print("{}  keys:{}".format(headerStr, keyStr))
        dRst = cInfo.SearchItem(headerStr, keyStr)
        cInfo.printSearch(dRst)


    # exit()
