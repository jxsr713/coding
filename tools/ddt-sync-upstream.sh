#########################################################################
# File Name: cp_files.sh
# Author: jxsr713
# mail: jxsr713@163.com
# Created Time: 2021年06月09日 星期三 15时10分45秒
#########################################################################
#!/bin/bash
path=`pwd`


echo "$#"

if [ $# -eq 0 ]; then
	echo "Please input domain name"
	exit
fi
module=$1

time=`date +"%m%d"`
branchName="ddt-$module-$time-wh"

check=`git branch -a | grep $branchName`

echo "Branch:$branchName ===>$check"

repo=`git remote -v | grep origin`

if [ ! "$repo" == "" ]; then
	echo $repo
else
	echo "Failed to find $repo on $path"
	exit 1
fi

echo "Set upstream!"

git remote add upstream  https://github.com/intel-innersource/os.linux.validation.ltp-ddt-for-ia

upstm=`git remote -v | grep upstream`
if [ ! "$upstm" == "" ]; then
	echo $upstm
else
	
	echo "Failed to find upstream on remote!"
	exit 1
fi

git fetch upstream

git checkout otc_ltp_ddt_DEV

git merge upstream/otc_ltp_ddt_DEV

git push origin otc_ltp_ddt_DEV

git checkout -b $branchName otc_ltp_ddt_DEV

#push new tree to remote
git push origin $branchName:$branchName


