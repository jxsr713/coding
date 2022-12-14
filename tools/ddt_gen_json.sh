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

src_path="./runtest/"

help(){
	cat << HELP
Usage:
	$0 [-s <source file>] [-m <module name>]
		-s: a test files under ./runtest/
		-i: show json files 
		-p: full path for test files 
		-d: show domain
		-f: feature
		-m: module name,the module used to match <module>_* files under ./runtest/

	domain and feature
	mce: domain=>Memory Feature=>MCE
	SAF: domain==>CPU  feature==>SAF
HELP

	exit 1
}

if [ $# -eq 0 ]; then
	help
fi


#opt list
OPT_LIST=""
while getopts "s:m:id:f:p:" opt; do
	case $opt in
		p)
			module=$OPTARG
			;;
		s)
			module="$src_path/$OPTARG"
			;;
		m)
			module="$src_path/${OPTARG}_*"
			;;
		i)
			show_json=1
			;;
		d)
			domain="${OPTARG}"
			OPT_LIST="${OPT_LIST} -m $domain"
			;;
		f)
			feature="${OPTARG}"
			OPT_LIST="${OPT_LIST} -f $feature"
			;;
		*)
			help
      exit 0
			;;
	esac
done


show_spec(){
	if [ $show_json -eq 0 ]; then
		return
	fi

	if [ $# -eq 0 ]; then
		return
	fi
	dir=$1
	echo "@@@@@$dir@@@@@@"
	for spec in ${dir}/*.json
	do
		echo "========SHOW ${spec##*/}======="
		echo "`cat $spec`"
	done
}


if [ "${module}" == "" ]; then
  help
fi

echo "${module}"
if [ -e "${module}" ]; then
  echo ${module}
else
  help
fi

files=`ls ${module} -l | awk '{ print $NF }' `

#遍历所有的test文件
for itm in $files; do
	echo "============Get $itm============"
	#get the dir name 
	#dir=`echo $itm | awk -F /  ' { print $NF} ' `
	dir=./json/${itm##*/}
	rm $dir -rf
	#echo $dir
	echo "python3 ${py_path}/gen_spec_json.py -s $itm $OPT_LIST "
	python3 ${py_path}/gen_spec_json.py -s $itm $OPT_LIST 
	# list the new json files
	ls $dir -l
	#tranlsate 4 ' ' to 2 ' '
	#the json in repo is 2 space
	#需要将以4个空格开头转变成2个空格，韩宁的工具生成的json的用2个空格
	sed -i "s/^    /  /g" $dir/*.json
	echo "Copy new files into ./runtest/spec/ from $dir"

	cp $dir/* ./runtest/spec/
	show_spec $dir
	echo "============  DONE  ============="
done

exit 

