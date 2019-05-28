
#默认还是用log来输出。今天体会到了

#文件操作##################################################################################################################
#编码问题 http://www.wklken.me/posts/2013/08/31/python-extra-coding-intro.html
#-*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
open(filename.decode('utf-8'), 'w') #打开中文文件名
s='中文' #utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312
print json.dumps(dict, encoding='UTF-8', ensure_ascii=False)
print str.encode('utf8')
#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。

#str是 字节                   串，由unicode经过编码(encode)后的字节组成的
#str  -> decode('the_coding_of_str') -> unicode
#unicode -> encode('the_coding_you_want') -> str

# 获取所有文件
def listdir(path, list_name):  #传入存储的list
	postfix = set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:
        	if file_path.split('.')[-1] in postfix:  
            	list_name.append(file_path)

#读文件
f.readlines() #将返回该文件中包含的所有行，不会自动换行
with open(filename) as f:
	for line in f:
    	print(line)
    	f.write('your line\n')
#输出##################################################################################################################
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
#菜鸟教程网址： www.runoob.com
print("%3d %0.2f" % (year, principal), file = f) #py3
print >> f, "%3d %0.2f" % (year, principal) #py2
#"./log/%s.log" % self.log_name