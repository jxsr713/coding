#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import re
import os


def test1():
    file_open = open('index.html', 'rb')
    try:
        content = file_open.read().decode('utf-8')
        print("======>", content)
        str1 = "href"
        reg = r'reference internal" href="(.+?)"'
        reg = r'reference internal" ' + str1 + '="(.+?)"'
        result = re.findall(reg, content)
        print("Result:", result)
        item = re.search(reg, content)
        print("Group:", item.group())
        # delete the same items in result
        if result is None:
            return

        temp = []

        [temp.append(i) for i in result if i not in temp]
        print("Temp:===>", temp)
        for line in temp:
            if '#' not in line and 'environment.html' in line:
                line = 'http://docs.openstack.org/liberty/install-guide-rdo/' + line
                print(line)
    #            os.system('wget ' + line)
    finally:
        file_open.close()


def test2():
    print("\n\n\n++++++Test2++++++++")
    file_open = open('index.html', 'rb')
    try:
        content = file_open.read().decode('utf-8')
        print("======>", content)
        reg = r'reference internal" href="(.+?)"'
        result = re.findall(reg, content)
        print("Result:", result)
    finally:
        file_open.close()
'''
: Search files in a directory include subdir with some keys.: record all result: show n lines before and after match line"
: provid function
:   files list (matched files)
:       matched lines in a file (2*n lines): show line number and content
: dict define:
    {file:{key:[ {line_num:[['before lines'],[lines], [after lines]]}, {line_num2:..........} ], key2 ......} , file1:{.....}, file2:{.....} }
    file: dict which is filename inlude path
        key: search key
        line_num: dict; line number which match key lines
            before_lines: list which record n lines content before matched line
            lines: list which record matched line
            after_lines: list which record n lines content after matched line
'''


class searchKeyInFiles(object):
    def __init__(self, path, keys):
        self.folder = path
        self.keys = keys
        self.DictFileContent = {}

    def ParserFile(self, filePath, keys):
        fileHandle = open(filePath, 'rb')

        regex = re.compile(keys)
        try:
            for line in fileHandle.readlines():
                line = line.decode('utf-8')
#                result = regex.findall(line)
                result = regex.search(line)
                if result is None:
#                    print("Failed to find!!!!")
                    continue

                print("===>", line)


#        reg = r'reference internal" href="(.+?)"'
#            pass
        finally:
            fileHandle.close()


def ParserFile(filePath):
    fileHandle = open(filePath, 'rb')

    try:
        lineNum = 0
        started = 0
        done = 0
        strEOR = ''
        for line in fileHandle.readlines():
            lineNum = lineNum + 1
            # Fixed error:can't use a string pattern on a bytes-like object
            line = line.decode('utf-8')
#                result = regex.findall(line)
            # remove '\n' char in start/end of string
            line = line.strip('\n')
            if started == 0:
                result = re.search(r'set tb_dict', line)
                if result is None:
                    continue
                started = 1
                continue

            result = re.search(r'^}', line)
            if result:
                print("=== stop parser!!!!")
                started = 0
                done = 1
                break

            startParser = 0
            line = line.strip('\\')
            line = line.strip('\t')
            print("###", line)
            result = re.search(r'}$', line)
            if result:
                startParser = 1

            strEOR = strEOR + line

            if startParser == 1:
                print("start parser EOR string:", strEOR)
                # regexp for finding chassis name
                regExp = re.compile(r'([\w|-]+) {')
                rstName = regExp.search(strEOR)
                if rstName:
                    print("=================\nName:", rstName.group(1))

                # regexp for finding sup1 condole ip and port
                regExp = re.compile(r'ts_IP_sup1 "([\d|.]+)" ts_line_sup1 "(\d+)"')
                resSup1 = regExp.search(strEOR)
                if resSup1:
                    print("IP:", resSup1.group(1), end='  ')
                    print("port:", resSup1.group(2))

                # regexp for finding sup2 condole ip and port
                regExp = re.compile(r'ts_IP_sup2 "([\d|.]+)" ts_line_sup2 "(\d+)"')
                resSup2 = regExp.search(strEOR)
                if resSup2:
                    print("IP:", resSup2.group(1), end=' ')
                    print("port:", resSup2.group(2))

                # regexp for finding apc ip and port
                regExp = re.compile(r'apc_port {([\d|.|\s|"]+)}')
                resApc = regExp.search(strEOR)
                if resApc:
                    print("APC:", resApc.group(1))

                # regexp for finding apc ip and port
                regPsu = re.compile(r'psu_cnt "(\d+)"')
                resPsu = regExp.search(strEOR)
                if resPsu:
                    print("PSU:", resPsu.group(1))

                strEOR = ''

#        reg = r'reference internal" href="(.+?)"'
#            pass
    finally:
        fileHandle.close()


if __name__ == '__main__':
    test1()
    test2()

    fileTest = searchKeyInFiles("index.html", "html")
    fileTest.ParserFile("index.html", "html")


    ParserFile("system_info.tcl")


