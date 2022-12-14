#a########################################################################
# File Name: .sh
# Author: jxsr713
# mail: jxsr713@163.com
# build kernel and gen rpm package
# Created Time: 2021年06月09日 星期三 15时10分45秒
#########################################################################
#!/bin/bash


#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#general source code can be used all shell script
#++++++++++++++++++++++++++++++++++++++++++++++++++++#
#get current path
CUR_DIR=`pwd`
echo "current path:$CUR_DIR"
#get current file location
TOOL_DIR="$( cd "$( dirname "$0"  )" && pwd  )"
echo "Tool path: $TOOL_DIR  $(dirname $0) $0"

######################################################
backup=0
remove=0

#----------------------------------------------------#
help(){
	cat << HELP
Usage:
	$0 [-k]
		gen rpm package
 		-b backup rpm packages
 		-c clear orig package to backup folder
HELP
	exit 1
}

get_opt(){
	echo "==========$*=========="
	while getopts "bc" opt; do
		echo "$opt!!!"
		case $opt in
			b)
				backup=1
				;;
			c)
				backup=1
				remove=1
				;;
			*)
				echo "===Wrong para $opt"
				exit 0
				;;
		esac
	done
}

get_opt $*

[[ -f ".config" ]] || {
		echo "Please check the config file!!!"
		exit 1
}

verstr=`grep "Version" ./binkernel.spec | awk '{print $2}'`
[ -z $verstr ] && {
		echo "Please check the version string!!!"
		exit 2
}

echo "Version:$verstr with back:$backup  remove:$remove"

sleep 3

make -j10 binrpm-pkg
[[ $? -eq 0 ]] || {
		echo "===========================FAILED:  Build ==========================="
		exit 3
}

dst=/home/weihong/rpmbuild/RPMS/x86_64/
echo "========================================================"
find /home/weihong/rpmbuild/RPMS/x86_64/ -name "*${verstr}*"


if [ $backup -eq 1 ]; then
		dst=./rpm-packages
		mkdir -p $dst
		find /home/weihong/rpmbuild/RPMS/x86_64/ -name "*${verstr}*" | xargs mv -t $dst
fi

if [ $remove -eq 1 ]; then
		echo "==+Remove####"
		find /home/weihong/rpmbuild/RPMS/x86_64/ -name "*${verstr}*" | xargs rm
fi

echo "================${dst}  : $verstr ================="
ls ${dst}/*$verstr* -rtal

