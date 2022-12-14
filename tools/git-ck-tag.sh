#########################################################################
# File Name:.sh
# Author: jxsr713
# mail: jxsr713@163.com
# Created Time: 2021年06月09日 星期三 15时10分45秒
#########################################################################
#!/bin/bash
#get current path
path=`pwd`
echo "current path:$path"
py_path=/workspace/tools/
#get current file location
CUR_DIR="$( cd "$( dirname "$0"  )" && pwd  )"
show_json=0
echo "Current command path: $CUR_DIR"

help(){
	cat << HELP
Usage:
	$0 [-t <tag name>]
HELP

	exit 1
}

if [ $# -eq 0 ]; then
	help
fi

#opt list
OPT_LIST=""
while getopts "t:m:id:f:" opt; do
	case $opt in
		t)
			tag=$OPTARG
			;;
		*)
			help
			;;
	esac
done


####################################################
#check the tag
rc=`git tag | grep $tag`
if [ ! $rc ]; then
	echo "Please check the tag:$tag"
	exit 1
fi

stmp=`date +"%Y%m%d"`

git checkout -b ${tag}_weihong_${stmp} $tag


