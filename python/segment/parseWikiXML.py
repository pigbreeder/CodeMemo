#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import os

def listdir(path, list_name):  #传入存储的list
	postfix = ['xml']#set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式
	for file in os.listdir(path):  
		file_path = os.path.join(path, file)  
		if os.path.isdir(file_path):  
			listdir(file_path, list_name)  
		else:  
			#if file_path.split('.')[-1] in postfix:
			if os.path.splitext(file_path)[1] == '.xml':
				list_name.append(file_path)
   	

def parseXML(filename, output):
	print('in file:',filename)
	DOMTree = xml.dom.minidom.parse(filename)
	collection = DOMTree.documentElement
	sentences = collection.getElementsByTagName('sen')
	line=1
	for sentence in sentences:
		jp = sentence.getElementsByTagName('j')[0].childNodes[0].data
		en = sentence.getElementsByTagName('e')
		print('line=' + str(line) + ' ' + jp.encode('utf8'))
		line += 1
		find = False
		for ee in en:
			if len(ee.childNodes) != 1:
				find = True
				break
			if ee.getAttribute('type') == 'check':
				#print('in check',ee.__dict__)
				#print('in check',ee.childNodes)
				find = True
				output.append((jp, ee.childNodes[0].data))
				break
		#print(sentence, 'no check')
		#print(en[0].__dict__)
		if not find:
			output.append((jp, en[0].childNodes[0].data))
file_list = []
#file_list = ['./GNM/GNM00155.xml','a.xml']
#import codecs
fail_file=[]
output = []
listdir('.', file_list)
for file in file_list:
	try:
		parseXML(file, output)
	except Exception as e:
		fail_file.append(file)
		print('occur exception',e)
with open('wiki.jp2en','w') as f:
	for line in output:
		#print(line[0]+'\t'+line[1],file=f)
		f.write(line[0].encode('utf8')+'\t'+line[1].encode('utf8')+'\n')
print('fail_files=',fail_file)
## 使用minidom解析器打开 XML 文档
#https://www.runoob.com/python/python-xml.html
#DOMTree = xml.dom.minidom.parse("movies.xml")
#collection = DOMTree.documentElement
#if collection.hasAttribute("shelf"):
#   print "Root element : %s" % collection.getAttribute("shelf")
# 
## 在集合中获取所有电影
#movies = collection.getElementsByTagName("movie")
# 
## 打印每部电影的详细信息
#for movie in movies:
#   print "*****Movie*****"
#   if movie.hasAttribute("title"):
#      print "Title: %s" % movie.getAttribute("title")
# 
#   type = movie.getElementsByTagName('type')[0]
#   print "Type: %s" % type.childNodes[0].data
#   format = movie.getElementsByTagName('format')[0]
#   print "Format: %s" % format.childNodes[0].data
#   rating = movie.getElementsByTagName('rating')[0]
#   print "Rating: %s" % rating.childNodes[0].data
#   description = movie.getElementsByTagName('description')[0]
#   print "Description: %s" % description.childNodes[0].data
