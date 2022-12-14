#########################################################################
# File Name: cscope.sh
# Author: jxsr713
# mail: jxsr713@163.com
# Created Time: 2021年04月06日 星期二 23时54分07秒
#########################################################################
#!/bin/bash
# 此脚本是用来自动生成cscope database文件的，把该脚本放在可执行环境中
# 以后我们在自己的项目代码目录中，直接使用source /bin/cscope.sh即可完成cscope环境的初始化，
#注意必须要使用source命令，这样才能够使cscope.sh中配置的CSCOPE_DB环境变量在本终端中始终可用。
#cscope.sh脚本同时支持多种命令，
#-d命令后可跟具体的项目代码目录，这样可以在其他目录生成对应项目的cscope数据库，
#-u是用来更新数据库的，
#-c是用来切换数据库的，如果我们有两个项目要切换，只需要进入到要切换的项目，
#目录中执行-c或者加上-d指明对应的目录即可。
#如果不加任何选项，那么cscope.sh默认就会在本目录下执行-u操作，也就是更新数据库操作，
#如果之前没有生成过数据库，那么它就会新生成一个数据库。
#所以正常使用下，我们只需要进入到我们的项目目录，然后执行cscope.sh脚本即可，
#为了更进一步的简化我们的处理，可以在~/.bashrc中添加环境变量：
#export PROJECT_INIT="source /bin/cscope.sh"
#这样我们进入到对应的项目，只需要执行$PROJECT_INIT即可自动调用到“source /bin/cscope.sh ”命令了，很简单了吧！

# check the parameter list
DIR=`pwd`
#if [ 1 -le $# ]; then
## the first para is the path
#	DIR=$1
#fi
#
#exit

# get the curent folder
update=1
change=0
while getopts "d:uc" opt;
do
    case $opt in
        d)
            DIR=$OPTARG
			;;
		u)
			update=1
			;;
		c)
			change=1
			;;
		?)
			echo "invaild option!"
			exit 1
	esac
done

cd ${DIR}

if [ 1 -eq ${change} ]; then
	echo "change project cscope database!"
	res=$(find ${DIR} -name cscope.out)
	if [ "x"${res} = "x" ]; then
		echo "Not found cscope database, generate cscope database!"
		find ${DIR} -name "*.h" -o -name "*.c" -o -name "*.cc" > cscope.files
		cscope -bkq -i cscope.files 
		ctags -R *
		export CSCOPE_DB=${DIR}/cscope.out
	else
		echo "Found cscope database:${res}, just change CSCOPE_DB env!"
		export CSCOPE_DB=${res}
	fi
elif [ 1 -eq ${update} ]; then
	echo "udpate project cscope database!"
	find ${DIR} -name "*.h" -o -name "*.c" -o -name "*.cc" > cscope.files
	cscope -bkq -i cscope.files
	ctags -R *
	export CSCOPE_DB=${DIR}/cscope.out
fi

echo CSCOPE_DB_PATH=${CSCOPE_DB}

