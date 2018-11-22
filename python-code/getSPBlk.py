#!/usr/bin/python3.3
import re
import os
# import paramiko
import sys

# find all super block and then set null to these block
# erse all super block

def ClearBackupSpBlk(dev):
    import string
    # cmdStr = "dumpe2fs " + dev + " | grep -E \"Backup superblock at\" | sed -n 's/.*superblock \(at [0-9]*\).*/\\1/p'"
    # find block size
    cmdStr = "mkfs.ext4 -n " + dev + " | grep -E \"Block size=\" | sed -n 's/.*=\([0-9]* \).*/\\1/p'"
    print(cmdStr)
    resultStr = os.popen(cmdStr).read()
    print("block size:" , resultStr)
    bs = int(resultStr)

    # find backup superblock
    cmdStr = "mkfs.ext4 -n " + dev + " | grep -E -A 1 \"Superblock backups\""
    print(cmdStr)
    resultStr = os.popen(cmdStr).read()

    # resultStr = "Backup superblock at 32768, Group daescriptors at 32769-32769 \n   Backup superblock at 98304, Group descriptors at 98305-98305 \n    Backup superblock at 163840, Group descriptors at 163841-163841"
    # result = re.findall(r'at (\d+)', resultStr)
    result = re.findall(r'(\d+)', resultStr)

    print("Back up SpBlk:", result)
    for lst in result:
        pos = int(lst)
        if pos < 0:
            continue
        # clear backup sp block
        cmdStr = "dd if=/dev/zero of=" + dev + " bs=" + str(bs) + " count=2 seek=" + str(pos)
        print(cmdStr)
        os.system(cmdStr)

    return 1;


if __name__ == '__main__':
    len = len(sys.argv)
    devStr = "/dev/sdb1"
    if len > 1:
        devStr = sys.argv[1]
    else:
        print("==" + sys.argv[0] + " <dev>  //dev: usb device file /dev/sdb1")
        exit(0)
    ClearBackupSpBlk(devStr)
