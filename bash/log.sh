#!/bin/bash
#可将log函数单独放一个文件，通过.命令引入，这样就可以共用了
#. log.sh 
#设置日志级别
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
# COLORS = { 
#     'WARNING': YELLOW,
#     'INFO': GREEN,
#     'DEBUG': WHITE,
#     'ERROR': RED 
# }   
loglevel=0 #debug:0; info:1; warn:2; error:3
logfile=$0".log"
function log {
    local msg;local logtype
    logtype=$1
    msg=$2
    datetime=`date +'%F %H:%M:%S'`
    #使用内置变量$LINENO不行，不能显示调用那一行行号
    #logformat="[${logtype}]\t${datetime}\tfuncname:${FUNCNAME[@]} [line:$LINENO]\t${msg}"
    logformat="[${logtype}]\t${datetime}\tfuncname: ${FUNCNAME[@]/log/}\t[line:`caller 0 | awk '{print$1}'`]\t${msg}"
    #funname格式为log error main,如何取中间的error字段，去掉log好办，再去掉main,用echo awk? ${FUNCNAME[0]}不能满足多层函数嵌套
    {  
    case $logtype in 
        debug)
            [[ $loglevel -le 0 ]] && echo -e "\033[1;34m${logformat}\033[0m" ;;
        info)
            [[ $loglevel -le 1 ]] && echo -e "\033[1;32m${logformat}\033[0m" ;;
        warn)
            [[ $loglevel -le 2 ]] && echo -e "\033[1;33m${logformat}\033[0m" ;;
        error)
            [[ $loglevel -le 3 ]] && echo -e "\033[1;31m${logformat}\033[0m" ;;
    esac
    } | tee -a $logfile
}
       
# lrun "ps -ef |grep ssh"
# get result:lrun_out
lrun() {             
    lrun_out=''      
    log info "in lrun params:$@"
    [[ $loglevel -ge 1 ]] && lrun_out=`eval $@`
}                    
                     
function check_sbatch_is_finished() {
    local sleep_num=100 
    sleep 2          
    local sid=`squeue|grep $1`
    log info "check_finished  $1 ."
    while :          
    do               
        if [[ "$sid" == "" ]]; then
            log info "sbatch $1 finished."
            break    
        fi           
                     
        sleep $sleep_num
        sid=`squeue|grep $1`
        log info "sbatch $1 is still running."
    done             
}                    

# https://www.jb51.net/article/108721.htm
# caller[expr] 没有指定expr时，显示当前子程序调用的行号和源文件名。如果expr是一个非负整数，显示当前子程序调用的行号、子程序名和源文件名。
# $LINENO 当前行号
# $FUNCNAME 表示函数的名字，它是一个数组变量，其中包含了整个调用链上所有的函数的名字，故变量${FUNCNAME[0]}代表shell脚本当前正在执行的函数的名字，而变量${FUNCNAME[1]}则代表调用函数${FUNCNAME[0]}的函数的名字
#以下为测试
debug () {
    log debug "there are $# parameters:$@"
}
info() {
    log info "funcname:${FUNCNAME[@]},lineno:$LINENO"
}
warn() {
    log warn "funcname:${FUNCNAME[0]},lineno:$LINENO"
}
error() {
    log error "the first para:$1;the second para:$2"
}
# set -x
# debug first second
# set +x
# info first second
# warn first second 
# error first second