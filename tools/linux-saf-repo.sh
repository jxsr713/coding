#########################################################################
# File Name: .sh
# Author: jxsr713
# mail: jxsr713@163.com
# sync km iommu code: saf driver and cli tool
# Created Time: 2021年06月09日 星期三 15时10分45秒
#########################################################################
#!/bin/bash
#get current path
path=`pwd`
echo "current path:$path"
py_path=/workspace/tools/
#get current file location
CUR_DIR="$( cd "$( dirname "$0"  )" && pwd  )"
echo "Current command path: $CUR_DIR"

if [ $# -eq 0 ]; then
	echo "Please input branch(rls or cli) name"
	exit
fi

branch=$1

case $branch in
	rls)
		remote="scan_at_field_release"
		local="saf-rls-0806"
		#git pull origin scan_at_field:saf-cli-0806
		#git checkout saf-cli-0806
		;;
	cli)
		remote="scan_at_field"
		local="saf-cli-0806"
		#git pull origin scan_at_field:saf-cli-0806
		;;
	*)
		echo "Wrong branch name: $$branch!(rls/cli)"
		exit 1
		;;
esac

match=`git branch -a | grep $remote`

if [ "$match" == "" ]; then
	echo "Not find remote branch:$remote"
	exit 1
fi

if [ "$local" == "" ]; then
	echo "Not find local branch:$remote"
	exit 1
fi

git checkout $local
git pull origin $remote:$local

git status



