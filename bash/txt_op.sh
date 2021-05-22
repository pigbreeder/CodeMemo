#!/bin/bash
# 读取文件
echo "$a" | while read i  
do  
  
done  

while read line
do
    ret=`grep -n $line tmp`
    if [[ $ret ]]; then
      echo $line
    fi
done < asdf

# 合并两行
paste -d "\t"  - - < filename
awk 'NR%2{printf "%s ",$0;next;}1' yourFile
sed 'N;s/\n/ /' yourFile
awk '{key=$0; getline; print key ", " $0;}'
# 交换两列
awk '{print $2,$1 > "id.txt"}' id.txt
# 分列输出
awk -F'\t' '{print $1>"file1"; print $2>"file2"}' file
awk 'NF' file # 去除空行

# 打印指定行
# print line number 52
sed -n '52p' # method 1
sed -n '20,40p;41q' file_name

# 打印指定列，倒数列
awk -F ':' '{print OFS="\t" $1,$4}' file
cat *|awk -F'\t' '{if($(NF-1) == "正常题目" && $NF == "否"){print $1"\t"$2"\t"$4}}'

# 字符串分割
echo $str | awk -F',' '{for( i=1;i<NF; i++ ) print $i}' 

str="hello,world,i,like,you,babalala"  
for i in `echo "$str" | sed 's/,/\n/g'`
do  
    echo $i  
done

# 查找utf8编码
grep -P -rn "[\x80-\xFF]" file
cat j2c_1217.sub.jp |sed '168783d;546003d' > j2c_1217.sub.sed.jp 

grep -P "[\x80-\xFF]" file.xml
https://stackoverflow.com/questions/3001177/how-do-i-grep-for-all-non-ascii-characters/3001626#3001626

#Cut=========================================================================
#https://www.cnblogs.com/dong008259/archive/2011/12/09/2282679.html
#-c ：以字符为单位进行分割，-d选项的默认间隔符就是制表符，-f取域。
echo $PATH | cut -d ':' -f 5 #以':'分割，第5个数据
#Sort========================================================================
# http://www.cnblogs.com/51linux/archive/2012/05/23/2515299.html
# -u 去除重复 -r降序 -n 要以数值来排序 -f 忽略大小写 -g 浮点数 -t 分隔符 -u 去除重复 -k 按照某个域进行 -r 反向 -d字典序 -n数字序 -M 月份序  -f 忽略大小写
sort:排序默认分隔符是tab和空格 若要指定使用 sort -t$'\t' a.txt
#grep=========================================================================
#egrep
#grep -o 仅输出匹配到的内容
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
grep -rio --exclude-dir={ece,pytorch,sys,proc} 'hello' /
-R 链接符号的文件也搜索
仅搜索单词 -w
egrep 'word1|word2'
grep -e 'word1' -e 'word2'
# 空白行
grep -n '^\s*$' 
#Sed=========================================================================
#sed -r 使用扩展正则 +?不用再加\
echo "Ã" | hexdump -C
echo "Ã" |sed 's/\xc3\x83/A/g'
# 替换匹配的文本中部分内容
sed 's/\(前一部分\)要替换的部分\(后一部分\)/\1替换后的字符串\2/' 
echo '123abc123' | sed 's/\([0-9]\{2,2\}\)[a-zA-Z]\{3,3\}\([0-9]\{3,3\}\)/\1aaa\2/' 
# 替换指定行内容，改变文件内容
var=hello
sed "4s/log.eval.batch.*/log.eval.batch.$var/g" 
# 对于路径中/的处理
sed -i "s#parent_dir=.*#parent_dir=${parent_dir}#g" ./basic.conf

sed -n 只打印受到影响的行
cat asdf
```
   src set "test" (1 docs, 2440 segs) 
  BLEU-SBP doc score using 4-grams = 0.3027 for system "yodao" on segment 1 of document "none" (13 words)

```
head asdf | sed -n 's/  BLEU-SBP.* = \(0.[0-9]\+\) for.* segment \([0-9]\+\) of .* "none" (\([0-9]\+\) words)/\1\t\2\t\3/gp'
cat $1|sed -n 's/.*BLEU-SBP.* = \(0.[0-9]\+\) .*\.\([0-9]\+\).sgm/\1\t\2/gp' | sort -k1 -n -r |head -n5
#Awk=========================================================================
#https://www.cnblogs.com/chengmo/tag/awk/
#$0	当前记录（作为单个变量）
#$1~$n	当前记录的第n个字段，字段间由FS分隔
#FS	输入字段分隔符 默认是空格 通过用 -F 传参设置   https://www.cnblogs.com/kingstarer/p/6059978.html
#    如果FS设置了不止一个字符作为字段分隔符，将作为一个正则表达式来解释，否则直接按该字符做为分隔符对每行进行分割。
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

#sort 连用
awk 'BEGIN{
a[100]=100;
a[2]=224;
a[3]=34;
for(i in a)
{print i,a[i] | "sort -r -n -k2";}
}'

# 统计每列最大长度
awk -F'\t' 'NR>1{cols=(cols<=NF?NF:cols); for (i=1; i<=NF; i++) max[i]=(length($i)>max[i]?length($i):max[i])} END {for (i=1; i<=cols; i++) printf "%d%s", max[i], (i==cols?RS:FS)}'

# 字符串中某个字符出现次数
# http://bbs.chinaunix.net/thread-1026122-1-1.html
echo "abcdabc1234abc" | awk -F'a' '{print NF-1}'

# 平均数 最大最小 中位数 计算
cat $file |grep "$prefix" |cut -d':' -f2|sort -n | awk '
  BEGIN {
    c = 0;
    sum = 0;
  }
  $1 ~ /^(\-)?[0-9]*(\.[0-9]*)?$/ {
    a[c++] = $1;
    sum += $1;
  }
  END {
    ave = sum / c;
    if( (c % 2) == 1 ) {
      median = a[ int(c/2) ];
    } else {
      median = ( a[c/2] + a[c/2-1] ) / 2;
    }
    for (i in a){ss += (a[i]-ave)^2} sd = sqrt(ss/c);
    OFS="\t";
    print "sum", "nums", "avg", "median", "sd", "min", "max";
    printf("%.2f\t%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f\n",sum, c, ave, median, sd, a[0], a[c-1]);
  }
'

# 统计单词个数
awk '{for(i=1;i<=NF;i++) a[$i]++} END {for(k in a) print k,a[k]}' testfile | sort -k 2 -n


################################ 去重汇总
# 根据某列去重
1 awk -F"," '!_[$1]++' file
2 sort -u -t, -k1,1 file
3 uniq -f1 file # 忽略某一行
uniq
cat <filename> | sort | uniq -d     # 只显示重复的行，每行只显示一次
cat <filename> | sort | uniq -D     # 只显示重复的行
cat <filename> | sort | uniq -i     # 忽略大小写
cat <filename> | sort | uniq -u     # 只显示只出现一次的行
cat <filename> | sort | uniq -c     # 统计每行重复的次数

去重第一列重复的行：
[root@localhost cc]# cat 2.txt |awk '!a[$1]++{print}'
adc 3 5
a d a

重复的行取最上面一行记录

去重以第一列和第二列重复的行：

[root@localhost cc]# cat 2.txt |awk '!a[$1" "$2]++{print}'
adc 3 5
a d a
a 3 adf

去除重复的行：

[root@localhost cc]# cat 2.txt |awk '!a[$0]++{print}'
adc 3 5
a d a
a 3 adf
a d b

只显示重复行：

[root@localhost cc]# cat 2.txt |awk 'a[$0]++{print}'
a 3 adf

################################  集合运算

用cat，sort，uniq命令实现文件行的交集 、并集、补集
交集 𝐹1∩𝐹2F1∩F2
cat f1 f2 | sort | uniq -d
并集 𝐹1∪𝐹2F1∪F2
cat f1 f2 | sort | uniq 
并集 - 交集 𝐹1-𝐹2
cat f1 f2 f2| sort | uniq -u
对称差，就是要找到两个集合放在一起，也只出现了一次的那些元素
cat f1 f2 | sort | uniq -u


join使用
主要是a1/2（左右连接），o（制定输出），1/2（指定连接的列）
https://www.cnblogs.com/agilework/archive/2012/04/18/2454877.html



# 打印行中有空白的情况
IFS=$'\n'
for i in `cat coder.txt`; do echo "$i"; done
unset IFS



# 从一个文件里面去重 过滤集合
https://unix.stackexchange.com/questions/299462/how-to-filter-out-lines-of-a-command-output-that-occur-in-a-text-file
grep -v -x -F -f forbidden.txt input.txt