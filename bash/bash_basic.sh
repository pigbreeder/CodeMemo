#!/bin/bash
set -x
curdir=`cd $(dirname $0);pwd`
#如果变量var没有被声明，那么就使用默认值，否则就是用var初始化的值
export CONF_PATH=${CONF_PATH:-"$curdir/../conf"} 
#配置文件
source $CONF_PATH/my.conf
#变量引号处理/连接起来
echo 'fuck'$fuck"fuck"
#默认程序
#source $curdir/common.sh
#
#1.${var:pos}：删除变量pos位置之前的字符。
#2.${var:pos:len}：从位置pos开始, 截取变量的len个字符。
#3.${var/Pattern/Replacement}：使用Replacement来替换变量var中第一个匹配Pattern的字符串。
#4.${var//Pattern/Replacement}：所有在变量var匹配Pattern的字符串, 都会被替换为Replacement。
#5.${var/#Pattern/Replacement}：如果变量var从开头开始的字符能匹配Pattern, 那么就使用Replacement来替换匹配到Pattern的字符串，否则保存var不变
#6.${var/%Pattern/Replacement}：如果变量var的后缀匹配Pattern, 那么就使用Replacement来替换匹配到Pattern的字符串

# https://blog.csdn.net/ljianhui/article/details/43128465
# var=/dir1/dir2/dir3/train_data/a.txt
# dirname=${var%/*}   dirname $var
# filename=${var##*/} basename $var
# file_suffix=${var##*.} basename $var .txt # basename without suffix
# #：表示从左边算起第一个
# %：表示从右边算起第一个
# ##：表示从左边算起最后一个
# %%：表示从右边算起最后一个
# 换句话来说，＃总是表示左边算起，％总是表示右边算起。
getTime(){
	now_day=`date '+%Y-%m-%d %H:%M'`
    last_time=`date -d"-1 ${task_frequency} ${now_day}" "+%Y-%m-%d %H:%M"`
    # 时间使用
	date -d '1d' "+%Y%m%d"
	date +%Y%m%d --date="-1 day"
	date +%Y%m%d --date="-1 month"
	date +%Y%m%d --date="+1 year"

	# Unix时间戳
	date +%s  #1559098555
	date -d '2010-2-22 22:14' +%s
	date -d @1361542596 +"%Y-%m-%d %H:%M:%S"
}
# 正则匹配
# 进行正则比对需要放在[[ ]]中，但是只有bash支持[[ ]]
# 正则不能加引号
regMatch(){
	#遍历文件夹,获取以.png结尾
	for file in *;do
	#echo $file
	reular="/*.mp3/"
	if [[ $file =~ (.*)png ]]; then
	#$path $file _$file
	echo $file
	echo #{$1}
	echo "0 ${BASH_REMATCH[0]}"
	echo "1 ${BASH_REMATCH[1]}"
	fi
done
re="http://([^/]+)/"
if [[ $name =~ $re ]]; then echo ${BASH_REMATCH[1]}; fi
}

array(){
	#声明
	a=(3 9 "234" 3.2 2 0 )
	b[0]='123'
	b[1]='345'
	#长度
	echo 'length:'${#a[@]}
	echo ${a[@]}
	echo ${a[0]}
	echo ${a[1]}
	echo ${a[2]}
	echo ${a[3]},${b[0]},${b[1]}

	filename=(`ls`)
	for var in ${filename[@]};do
	echo $var
	done
}
function calc(){
	#加法：
	n=10
	let n=n+1
	echo $n #n=11
	#乘法：
	let m=n*10
	echo $m
	#除法：
	let r=m/10
	echo $r
	#求余数：
	let r=m%7
	echo $r
	let r=m**2
	echo $r
}
function str(){
	str='hello world'
	echo ${#str}
	echo 'Alex'|awk '{print length($0)}'
}
function controlFlow(){
	#"[ -z $STRING ]" #空为真 -n 空为假
	#-e 文件存在 -f 正常文件（非目录） -d 目录
	#-eq 等于,如:if [ "$a" -eq "$b" ] 
	#-ne 不等于,如:if [ "$a" -ne "$b" ] 
	#-gt 大于,如:if [ "$a" -gt "$b" ] 
	#-ge 大于等于,如:if [ "$a" -ge "$b" ] 
	#-lt 小于,如:if [ "$a" -lt "$b" ] 
	#-le 小于等于,如:if [ "$a" -le "$b" ] 
	#
	#= 等于,如:if [ "$a" = "$b" ] 
	#== 等于,如:if [ "$a" == "$b" ],与=等价

	a=10
	b=20
	if [ $a == $b ]; then
	   echo "a 等于 b"
	elif [ $a -gt $b ]; then
	   echo "a 大于 b"
	elif [ $a -lt $b ]; then
	   echo "a 小于 b"
	else
	   echo "没有符合的条件"
	fi
##################################################
	int=1
	while(( $int<=5 ))
	do
	    echo $int
	    let "int++"
	done

	# while true
	# 	do
	# 	    command
	# 	done
}
# function==================================================================
# $#	传递到脚本的参数个数
# $*	以一个单字符串显示所有向脚本传递的参数
# $$	脚本运行的当前进程ID号
# $!	后台运行的最后一个进程的ID号
# $@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
# $-	显示Shell使用的当前选项，与set命令功能相同。
# $?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
funWithReturn(){
     echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
#funWithReturn
echo "输入的两个数字之和为 $? !"
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
#funWithParam 1 2 3 4 5 6 7 8 9 34 73


#getopts option_string variable 
#当optstring以”:”开头时，getopts会区分invalid option错误和miss option argument错误。
#invalid option时，varname会被设成?，$OPTARG是出问题的option； 
#miss option argument时，varname会被设成:，$OPTARG是出问题的option。 
#如果optstring不以”:“开头，invalid option错误和miss option argument错误都会使varname被设成?，$OPTARG是出问题的option。 
while getopts "a:b:cdef" opt; do
  case $opt in
    a)
      echo "this is -a the arg is ! $OPTARG" ;;
    b)
      echo "this is -b the arg is ! $OPTARG" ;;
    c)
      echo "this is -c the arg is ! $OPTARG" ;;
    \?)
      echo "Invalid option: -$OPTARG"; exit 1;;
  esac
done
echo -e ${@} '\t tot=' $#
echo "OPTIND is $OPTIND" #OPTARG中存储选项后面的参数，OPTIND为处理的参数的总的个数。