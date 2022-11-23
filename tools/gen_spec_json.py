#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import time
import getopt
import os

import re

false="false"
debug = 0
domain="CPU"
feature="FEATURE"
scenario=""

dst_path=""

argc = len(sys.argv)
if argc <= 1:
    print("Please input a test file!");
    exit();

spec_json = {
 "name": "",
 "cmdline": "",
 "summary": "",
 "priority": "P1",
 "scenario": "",
 "domain": "CPU",
 "feature": "SAF",
 "owner": "weihongz",
 "testType": "",
 "execType": "Auto",
 "poweron": False,
 "presilicon": True,
 "clientOnly": False,
 "serverOnly": False,
 "kparams": [],
 "kconfigs": [],
 "packages": [],
 "bios": [],
 "peripherals": [],
 "createDate": time.strftime("%Y-%m-%dT%H:%M:%S.000-0000", time.localtime()),
 "link": "",
 "tips": ""
}

def init_json():
    spec_json["name"] = ""
    spec_json["cmdline"] = ""
    spec_json["summary"] = ""
    spec_json["priority"] = "P1"
    spec_json["scenario"] = scenario
    spec_json["domain"] = domain
    spec_json["feature"] = feature
    spec_json["owner"] = "weihongz"
    spec_json["testType"] = "",
    spec_json["execType"] = "Auto"
    spec_json["poweron"] = False
    spec_json["presilicon"] = True
    spec_json["clientOnly"] = False
    spec_json["serverOnly"] = False
    spec_json["kparams"] = []
    spec_json["kconfigs"] = []
    spec_json["packages"] = []
    spec_json["bios"] = []
    spec_json["peripherals"] = []
    spec_json["createDate"] = time.strftime("%Y-%m-%dT%H:%M:%S.000-0000", time.localtime())
    spec_json["link"] = ""
    spec_json["tips"] = ""

#check the name format: <Test_Object_Name>_<Execution_Time>_<Test_Type>_<Description>
#mainly check the 3rd field: FUNC/FUNC_NEG.....
#return None or match list
def check_test_case_name(testname):
    test_type_list = ["FUNC", "FUNC_NEG", "PERF", "STRESS"]
    matched = re.findall( r"^[A-Z|0-9]+_[A-Z|0-9]+_([A-Z]+)_\w*", testname)
    if not matched:
        return None
    if not matched[0] in test_type_list:
        return None

    return matched


#if the json file is existed in spec folder, then load the spec
def load_json(filename):
    global spec_json
    json_path = "./runtest/spec/" + filename + ".json"
    if not  os.path.exists(json_path):
        print("[INFO] Create a new spec file:" + json_path)
        init_json();
        return

    print("[INFO] load spec file:" + json_path)

    with open(json_path) as f:
        spec_json = json.load(f)


    return;


#print information
def print_debug_info(info):
    if debug == 1:
        print(info)


def get_scenario(filename):
    global scenario
    pos = filename.rfind("/")
    if(pos < 0):
        scenario = filename
    else:
        scenario = filename[pos + 1 : ]

    #spec_json["scenario"] = scenario
    return;


def parser_cmdline(cmdline):
    global domain, feature
    cmdline.replace('\n', '').replace('\r', '')
    pos = cmdline.find(" ")
    if( pos < 0):
        return;
    name = cmdline[0:pos].strip()
    print("######################################################" \
            "\nGet file:%s" % (name));
    #check if the file existed
    #print(spec_json);
    load_json(name)
    print(spec_json);

    # check the name format
    matched = check_test_case_name(name)
    if matched:
        spec_json["testType"] = matched[0]
    else:
        print("Please check the format of test cases name: %s" % (cmdline));

    cmd = cmdline[pos:].strip()
    spec_json["name"] = name

    spec_json["cmdline"] = cmd
    if domain:
        spec_json["domain"] = domain

    if feature:
        spec_json["feature"] = feature

    print_debug_info("Get %s %s \n\rfrom %s" % (name, cmd, cmdline))
    return;

def save_json(spec):
    global dst_path
    if spec["name"] == "":
        return;
    #with open(spec_json["scenario"] + "/" +  spec["name"]+".json", "w") as fp:
    with open(dst_path + "/" +  spec["name"]+".json", "w") as fp:
        js = json.dumps(spec)
        fp.write(json.dumps(spec, indent=4))
    return;

def parser_test_file(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            #print("Get line:" + line)
            line.strip()
            pos = line.find("@desc")
            if( pos != -1):
                print_debug_info("Get line:" + line)
                spec_json["summary"] = line[pos + 5:].strip()
            if(line[0] != '#'):
                parser_cmdline(line)
                if spec_json["name"] == "":
                    continue

                print_debug_info(spec_json);
                save_json(spec_json)
                #restore some fields
                #spec_json["name"] = ""
                #spec_json["cmdline"] = ""

    return;

#check the dir, and generate the folder
def check_gen_dir():
    import os
    global dst_path
    dst_path = "./json/" + scenario
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    return;


if __name__ == "__main__":
    opts,args = getopt.getopt(sys.argv[1:],
            '-h-s:-v-d-m:-f:',
            ['help','dir=','version','debug', 'domain', 'feature'])
    srcfile = None

    print(opts)
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("[*] Help info")
            sys.exit()
        if opt_name in ('-v','--version'):
            print("[*] Version is 1.0 (2021/10/21)")
            sys.exit()
        if opt_name in ('-s','--src'):
            srcfile = opt_value
            print("[*] dir is ",srcfile)
            # do something
        if opt_name in ('-d','--debug'):
            debug = 1
            print("[*] debug is ", debug)
        if opt_name in ('-m','--domain'):
            domain = opt_value
            print("[*] debug is ", domain)
        if opt_name in ('-f','--feat'):
            feature = opt_value
            print("[*] feature is ", feature)

    if srcfile is None :
        print("Please input source dir: -s <dir>")
        sys.exit()

    get_scenario(srcfile)
    check_gen_dir()
    parser_test_file(srcfile)
