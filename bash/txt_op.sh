#!/bin/bash
# 合并两行
paste -d "\t"  - - < filename
awk 'NR%2{printf "%s ",$0;next;}1' yourFile
sed 'N;s/\n/ /' yourFile
awk '{key=$0; getline; print key ", " $0;}'

awk 'NF' file # 去除空行
#Cut=========================================================================
#https://www.cnblogs.com/dong008259/archive/2011/12/09/2282679.html
#-c ：以字符为单位进行分割，-d选项的默认间隔符就是制表符，-f取域。
echo $PATH | cut -d ':' -f 5 #以':'分割，第5个数据
#Sort========================================================================
# http://www.cnblogs.com/51linux/archive/2012/05/23/2515299.html
# -u 去除重复 -r降序 -n 要以数值来排序 -f 忽略大小写
sort:排序默认分隔符是tab和空格 若要指定使用 sort -t$'\t' a.txt
#grep=========================================================================
#egrep
#-c：只输出匹配行的计数。
#-I：不区分大 小写(只适用于单字符)。
#-h：查询多文件时不显示文件名。
#-l：查询多文件时只输出包含匹配字符的文件名。
#-n：显示匹配行及 行号。
#-s：不显示不存在或无匹配文本的错误信息。
#-v：显示不包含匹配文本的所有行。
#pattern正则表达式主要参数：
#\： 忽略正则表达式中特殊字符的原有含义。
#^：匹配正则表达式的开始行。
#$: 匹配正则表达式的结束行。
#\<：从匹配正则表达 式的行开始。
#\>：到匹配正则表达式的行结束。
#[ ]：单个字符，如[A]即A符合要求 。
#[ - ]：范围，如[A-Z]，即A、B、C一直到Z都符合要求 。
#.  ：所有的单个字符。
#* ：有字符，长度可以为0。
#\< 相当于\b 



#Awk=========================================================================
#https://www.cnblogs.com/chengmo/tag/awk/
#$0	当前记录（作为单个变量）
#$1~$n	当前记录的第n个字段，字段间由FS分隔
#FS	输入字段分隔符 默认是空格
#NF	当前记录中的字段个数，就是有多少列
#NR	已经读出的记录数，就是行号，从1开始
#RS	输入的记录他隔符默 认为换行符
#OFS	输出字段分隔符 默认也是空格
#ORS	输出的记录分隔符，默认为换行符
#ARGC	命令行参数个数
#ARGV	命令行参数数组
#FILENAME	当前输入文件的名字
#正则  ~  !~ 匹配/不匹配
awk 'BEGIN{info="this is a test";if( info ~ /test/){print "ok"}}'
awk 'length>80' file #从file文件中找出长度大于80的行

#输出单引号
awk '{print "'\''"}'  因为'中不能使用跳脱符 同理： a='asdf'\''fdas'
awk '{print "\""}' 
#正则  ~  !~ 匹配/不匹配
awk 'BEGIN{info="this is a test";if( info ~ /test/){print "ok"}}' 
#1. sub函数 sub函数只实现第一个位置的替换，gsub函数实现全局的替换。
echo "a b c 2011-11-22 a:d" | awk 'sub(/-/,"",$4)'
#a b c 201111-22 a:d
#2. gsub函数
echo "a b c 2011-11-22 a:d" | awk 'gsub(/-/,"",$4)'
#a b c 20111122 a:d
#连接操作：
数字     awk 'BEGIN{a="100";b="10test10";print (a+b+0);}'
字符串 awk 'BEGIN{a=100;b=100;c=(a""b);print c}' 
#打印指定行后的内容
#倒数第几行NF-2
for line in `ls -F|grep "data.*\.txt$"`; do
	cat $line |awk -F'：' '{
	 if ($0 ~ /^@/) 
	 	next ; 
	 else 
	 	for(i=2;i<=NF;i++)
	 		printf $i",";
	 	printf "\n" 
	}'
done
#统计连接数
netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

#统计平均值等：
grep "takes" voice-call-guanyun.log | cut -d' ' -f20 | awk '
BEGIN{
    min=1000;max=0;tot=0;cnt=0;
}
{
    if(max < $0){
        max=$0;
    }
    if(min>$0){
        min=$0;
    }
    tot +=$0;
    cnt+=1;
}
END{
    printf ("max=%d,min=%d,avg=%d\n",max,min,tot/cnt);
}'
#sort 连用
awk 'BEGIN{
a[100]=100;
a[2]=224;
a[3]=34;
for(i in a)
{print i,a[i] | "sort -r -n -k2";}
}'

#Sed=========================================================================

echo "Ã" | hexdump -C
echo "Ã" |sed 's/\xc3\x83/A/g'


uniq:重复内容只显示一次 去除排序过的文件中的重复行
wc:统计单词数  行数 单词数 字符数
tee:双向重定向
tr:删除或替换数据col:转化为纯文本join:将两个文件中相关信息放在一起
cat paste:行合并；列合并
split:将大文件传为小文件