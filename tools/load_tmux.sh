#########################################################################
# File Name: /home/weihong/bin/load_tmux.sh
# Author: jxsr713
# mail: jxsr713@163.com
# Created Time: 2021年04月15日 星期四 17时23分48秒
#########################################################################
#!/bin/bash

prog=`basename $0`

function usage() {
	echo "====================================="
	echo "load tmux session!"
	echo "$prog <session name>"
	echo "====================================="

}

if [ $# -eq 0 ]; then
	echo "Please enter a tmux session"
	tmux ls
	usage
	exit 0
fi

# check the session existed!!!!
sName=$1
matched=`tmux ls | grep $sName`
echo "===$matched"
if [ ! -n "$matched" ]; then
	tmux ls
	exit 0
fi

# 确认是否已经attached
#判断是否有attached的字串，判断session是否已经attached
if [[ $matched =~ "attached" ]]; then
	echo "$sName was attached !!! Please check it!"
	exit 0
fi

tmux a -t $sName



