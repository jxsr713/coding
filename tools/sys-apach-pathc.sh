#!/bin/bash
#########################################################################
# File Name: sys-apach-pathc.sh
# Author: weihong
# mail: 
# Created Time: 2021年12月27日 星期一 10时01分47秒
#########################################################################

[[ "$(sudo awk -F ':' '{print $1;}' /etc/passwd|grep sys_certiagsgar)" ]] && {
		echo "sys_certiagsgar already created"
		exit
}

sudo rm -rf /tmp/iags/
mkdir -p /tmp/iags/
cd /tmp/iags/
git clone https://gitlab.devtools.intel.com/kmartin1/nexpose-iags-public-key-scripts.git
cd nexpose-iags-public-key-scripts
cd GAR
sudo chmod a+x add_iags_gar_pubkey.sh
sudo ./add_iags_gar_pubkey.sh

cd /tmp
sudo rm -rf /tmp/iags/

