#!/bin/bash



curdir=`cd $(dirname $0);pwd` #进入执行脚本的路径并返回
basename filename #得到文件名

#随机数据分开
shuf source.txt > source_shuffle.txt


#【一】从第3000行开始，显示1000行。即显示3000~3999行
cat filename | tail -n +3000 | head -n 1000
#【二】显示1000行到3000行
cat filename| head -n 3000 | tail -n +1000
#分解：
tail -n 1000 #显示最后1000行
tail -n +1000 #从1000行开始显示，显示1000行以后的
head -n 1000 #显示前面1000行
#【三】用sed命令
sed -n '5,10p' filename #这样你就可以只查看文件的第5行到第10行。

#find========================================================================
#查找所有".h"文件中的含有"helloworld"字符串的文件（组合命令）
find /PATH -name "*.h" -exec grep -in "helloworld" {} \;
#获取文件夹
folders=`ls -F|grep '\/$' `
#进入文件夹获取文件 or:`ls -F|grep -v '\/$' `
for folder in $folders; do
        cd $folder
        folder=${folder%/}  #去掉末尾/
        echo "in $folder"
        pwd
        for file in `ls -F|grep "^${folder}.*txt$"`; do
                echo $file
                tail -n+3 $file >> ../${folder}.jp
        done
        cd -
done
#join命令####==================================================================
功能：“将两个文件里指定栏位同样的行连接起来”，即依照两个文件里共有的某一列，将相应的行拼接成一行。
join [options] file1 file2
注：这两个文件必须在已经在此列上是依照同样的规则进行了排序。
join选项
-a FILENUM：除了显示匹配好的行另外将指定序号（1或2）文件里部匹配的行显示出来
-e EMPTY：将须要显示可是文件里不存在的域用此选项指定的字符取代
-i :忽略大写和小写
-j FIELD ：等同于 -1 FIELD -2 FIELD,-j指定一个域作为匹配字段
-o FORMAT：以指定格式输出
-t CHAR ：以指定字符作为输入输出的分隔符
join 默认以空白字符做分隔符（空格和\t）,能够使用 join -t $'\t'来指定使用tab做分隔符
-v FILENUM：与-a相似 但值显示文件里没匹配上的行
-1 FIELD：以file1中FIELD字段进行匹配
-2 FIELD：以file2中FIELD字段进行匹配
--help ：打印命令帮助文件
样例：
文件 file1.txt
aa 1 2
bb 2 3
cc 4 6
dd 3 3
文件file2.txt
aa 2 1
bb 8 2
ff 2 4
cc 4 4
dd 5 5
1.join file1.txt file2.txt
输出：aa 1 2 2 1
bb 2 3 8 2
默认已两个文件的第一行做匹配字段，默认以空格（不限个数）做分隔符。
2.join -j 1 file1.txt file2.txt
输出：aa 1 2 2 1
bb 2 3 8 9
-j选项 指定了以两个文件里第一列做匹配字段 等同于join file1.txt file2.txt
3. join -1 2 -2 3 file1.txt file2.txt
输出： 1 aa 2 aa 2
2 bb 3 bb 8
4 cc 6 ff 2 
4 cc 6 cc 4
以第一个文件的第二列和第二个文件的第三列做匹配字段。因为第二个文件里第三列的两个3 都与第一个文件里第三行因此输出
4 cc 6 ff 2 
4 cc 6 cc 4
4 join -o 1.1 -o 1.2 -o 1.3 -o 2.1 -o 2.2 -o 2.3 -e 'empty' -a 1 file1.txt file2.txt 
输出： aa 1 2 aa 2 1
bb 2 3 bb 8 2
cc 4 6 empty empty empty
dd 3 3 empty empty empty
-o 指定 将file1的1,2,3列，file2的1,2,3 列都输出。-a指定将file1中不匹配的行也输出，可是file2中沒有与file1后两行相应的字段，因此使用empty补齐。
5.join -v 1 file1.txt file2.txt 
输出： cc 4 6
dd 3 3
-v 1 将file1中不匹配的行输出
PS：join命令和数据库中的join命令很相似。
尽管file1和file2都已经排序，可是因为在第三行时開始不匹配因此仅仅匹配上了前两行，后面的行尽管字段也能够相应可是以不能匹配。join命令，对文件格式的要求很强，假设想要更灵活的使用，可用AWK命令，參加AWK实例
6. join 标准输入
有时我们须要将多个格式同样的文件join到一起，而join接受的是两个文件的指令，此时我们能够使用管道和字符"-"来实现
join file1 file2 | join - file3 | join - file4 
这样就能够将四个文件 连接到 一起了。



uniq:重复内容只显示一次 去除排序过的文件中的重复行
wc:统计单词数  行数 单词数 字符数
tee:双向重定向
tr:删除或替换数据col:转化为纯文本join:将两个文件中相关信息放在一起
cat paste:行合并；列合并
split:将大文件传为小文件