#!/bin/bash
#less -r 是看控制字符   #先用U再用r会有改变否则没啥变化
less -U 是将tab回车看成控制字符
cat -Te filename # man cat
vim 输入 Ctrl+V + 十进制



jobs, fg, bg, kill, C-z &
http://www.cnblogs.com/mfryf/archive/2012/05/09/2491322.html
jobs -l 查看运行进程，可以kill掉
& 类似并行，放在后台执行
nohup 这个不受控制台控制，输出内容nohup.out

后台运行(nohup mqnamesrv  >/dev/null 2>&1)&

这样可以让程序并行执行 并且让输出到空的设备上 并重定向错误到标准输出，也输入到空

nohup执行python程序时，print无法输出
nohup python -u test.py > nohup.out 2>&1 &



#查看端口
netstat -apn|grep your_port

#jps 查看Java程序
#查看线程状况
pstree -p [pid]
top -Hp pid