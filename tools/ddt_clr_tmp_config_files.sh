#########################################################################
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

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
CFG_DIR="./bk-config-${TIMESTAMP}"
mkdir -p ${CFG_DIR}
mv config* ${CFG_DIR}
rm conf* -rf
cp ${CFG_DIR}/* ./ -rf
exit 




