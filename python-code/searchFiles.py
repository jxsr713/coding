#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import os
import sys
# ignore binary files
listonly = False
skipexts = ['.gif' , '.exe' , '.pyc' , '.o' , '.a' , '.dll' , '.lib' , '.pdb' , '.mdb']


def visitfile(fname, searchKey):
    global fcount, vcount

    try:
        if not listonly:
            if os.path.splitext(fname)[1] in skipexts:
                pass
            elif open(fname).read().find(searchKey) != -1:
                print('%s has %s' % (fname, searchKey))
                fcount += 1

    except:
        pass
    vcount += 1


def visitor(args, directoryName, filesInDirectory):     # called for each dir
    for fname in filesInDirectory:
        fpath = os.path.join(directoryName, fname)
        if not os.path.isdir(fpath):
            visitfile(fpath, args)


def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    os.path.walk(startdir, visitor, searchkey)

if __name__ == '__main__':
    root = input("type root directory:")
    key = input("type key:")
    searcher(root, key)
    print('Found in %d files, visited %d'%(fcount, vcount))
