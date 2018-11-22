#!/usr/bin/env python

'string example -- creaet a new text file'

import os
import sys

ls = os.linesep


def IntipToStripAndReverse():
    ipint = 111222123123
    ipstr = str(ipint)
    ipreturn = ipstr[0:3]+'.'+ipstr[3:6]+'.'+ipstr[6:9]+'.'+ipstr[9:12]
    print "%d-->%s" % (ipint, ipreturn)

    ipint = 0
    iplist = ipreturn.split(".")
    ipstr = "".join(iplist)
    ipint = int(ipstr)
    print "%s-->%s-->%d" % (ipreturn, iplist, ipint)


def newTextFile():
    # get filename
    while True:
        fname = raw_input("name:")
        if os.path.exists(fname):
            print "Errors: '%s' already exist" % fname
        else:
            break
    # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

    # loop until user terminates input
    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)
    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'Done'


def DictExmNewUser(db):
    #    db = {}
    promt = 'login desired:'
    while True:
        name = raw_input(promt)
        if db.has_key(name):
            promt = 'name taken, try another:'
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db[name] = pwd


def DictExmOldUser(db):
    name = raw_input('Login: ')
    pwd = raw_input('Passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'


def DictExmDelUser(db):
    promt = 'Delete user:'
    while True:
        name = raw_input(promt)
        if db.has_key(name):
            promt = "delete user %s (y/n)" % name
            dele = raw_input(promt)
            if dele == 'y':
                del db[name]
            break
        else:
            print "invalid user"
            break


def DictExmShowmenu():
    promt = """
(N)ew User Login
(E)xisting User Login
(D)elete User
(Q)uit
Enter choice:"""

    db = {}
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(promt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neqd':
                print 'invalid option , try again'
            else:
                chosen = True
        if choice == 'd':
            DictExmDelUser(db)
        if choice == 'q':
            done = True
        if choice == 'n':
            DictExmNewUser(db)
        if choice == 'e':
            DictExmOldUser(db)


def DictMerge():
    print '\n\nMerge two dict and print '
    dict1 = {1: 'a', 2: 'b'}
    dict2 = {3: 'a', 1: 'b', 'a': 'asd'}
    dict2.update(dict1)

    keylst = dict2.keys()
    print 'keys:%s' % keylst
    keylst.sort(reverse=True)
#    dict3 = dict1 + dict2
    print 'dict1:%s' % dict1
    print 'dict2:%s' % dict2
    print 'keys:%s' % keylst
    for k in keylst:
        print 'keys', k, ' value:', dict2[k]
#    print 'dict3:%s' % dict3


def DictFrom2List():
    print '\nCreate a dict fron two list: keylist and valuelist'
    keyslst = ['a', 'b', 'c', 'z', 'f']
    valslst = ['1', '3', '6', '9', '2']

    db = {}
    print keyslst
    print valslst
    for idx in range(len(keyslst)):
        db[keyslst[idx]] = valslst[idx]

    print db


def os_example():
    for tmpdir in ('/tmp', r'c:/temp'):
        if os.path.isdir(tmpdir);
            break
        else:
            print 'No temp directory available'


print "Python:Zhawh Note"
DictMerge()
DictFrom2List()
sys.exit(1)
DictExmShowmenu()
IntipToStripAndReverse()
sys.exit(1)
