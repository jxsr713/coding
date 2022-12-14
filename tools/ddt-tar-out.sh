#a########################################################################
# File Name: .sh
# Author: jxsr713
# mail: jxsr713@163.com
# sync km iommu code: saf driver and cli tool
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
skip=1
src_dir=$CUR_DIR
dst_dir=""
symbol=""

#----------------------------------------------------#
help(){
	cat << HELP
Usage:
	$0 [-k]
		gen package 
 		-k skip pmu/tdx large files]
 		-s ddt out/latest source folder
		-d dst folder
		-f feature name
HELP
	exit 1
}

get_opt(){
	echo "==========$*=========="
	while getopts "k:s:f:d:" opt; do
		echo "$opt!!!"
		case $opt in

			s)
				src_dir=$OPTARG
				;;
			k)
				skip=1
				;;
			d)
				dst_dir=$OPTARG
				;;
			f)
				symbol="-$OPTARG"
				;;
			*)
				echo "===Wrong para $opt"
				exit 0
				;;
		esac
	done
}


#######################################################
skip_files() {
	find ./ -name pmu_test_suite.tar | xargs rm -rf
	find ./ -name tdx_img.tgz | xargs rm -rf
	return
}

######################################################
# check ddt binary folder
# some build scripts should not in the folder
######################################################
check_ddt_bin_folder() {
		#check ddt folder
		[[ -f "${src_dir}/clkv" ]] || {
			echo "please make sure $src_dir is ddt folder!"
			return 1
		}
		#check if the folder is dev folder
		[[ -d "${src_dir}/bin" && -d "${src_dir}/share" ]] || {
			echo "please make sure $src_dir is ddt's out folder!"
			return 1
		}

		return 0
}


[ $# -eq 0 ] && help

get_opt $*

[ -z "$src_dir" ] && help
[ -d "$src_dir" ] || {
	echo "Please make sure $src_dir exist!"
	exit 1
}
echo "Source out folder: $src_dir!!!"

[ -z $dst_dir ] && {
		cur=`pwd`
		cd $src_dir/..
		dst_dir=`pwd`
		cd $cur
}
echo "Destination folder: $dst_dir!!!"



check_ddt_bin_folder
[ $? -eq 0 ] || exit 0

[ -d "$dst_dir" ] || {
	echo "Please make sure ====>>>> $dst_dir exist!"
	exit 0
}

[ $skip -eq 1 ] && skip_files

stmp=`date  +"%m%d-%H%M%S"`

echo "goto $src_dir"

sleep 5

cd $src_dir
pwd
echo "tar -cvzf $dst_dir/ddt${symbol}-$stmp.tgz ./*"

tar -cvzf $dst_dir/ddt${symbol}-$stmp.tgz ./*


echo -e "\E[34m=========== TAR DONE!!! =  please get the file in =============="

file=`readlink -f  $dst_dir/ddt${symbol}-$stmp.tgz`
echo -e "\E[32m=======${file}=======\n\E[0m"

exit 0

