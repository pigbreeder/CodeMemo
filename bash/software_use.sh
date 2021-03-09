#!/bin/bash
#less -r 是看控制字符   #先用U再用r会有改变否则没啥变化
=  临时显示百分比，文件名
-M 显示百分比，文件名 
-N 显示行号
-U 查看特殊控制字符


cat -Te filename # man cat
vim 输入 Ctrl+V + 十进制
去除^M   %s/\r$//
Ctrl + L 重新渲染
查看不可见字符
:set invlist/list
# 查找匹配的有多少个
:%s/pattern/&/g
# & 代表的意思就是用来表示前面比对的字串，所以做这个指令其实对档案本身并不会有什麽改变。但是由於做的是全域的取代置换， vim 会告诉你有从多少行中多少个字串被取代。轻轻松松很漂亮地用一行命令解决这个问题。

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

# 文件标识符，用这个命令在文件夹目录下run
find -type f -exec sha1sum {} \; | sort | sha1sum | head -c 5 && echo

alias cuda8='cuda8(){ export CUDA_HOME=/usr/local/cuda-8.0;export CUDA_ROOT=$CUDA_HOME;export PATH=$CUDA_HOME/bin:$PATH;export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH;export LIBRARY_PATH=$CUDA_HOME/lib64:$LIBRARY_PATH;};cuda8'
 
#集合操作
sort uniq
sort <file1> <file2> | uniq -d      # 交集
sort <file1> <file2> | uniq         # 并集
sort <file1> <file2> <file2> | uniq -u  # 差集
sort <file1> <file2> | uniq -u  # 对称差，找到两个集合放在一起，也只出现了一次的那些元素