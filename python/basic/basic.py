#!/usr/bin/env python
# encoding: utf-8
# 
# 加载顺序
# 能被 import 的包括：package，package 中的模块，模块中的变量。影响 import 的属性是 __all__， __all__ 是个list，能够影响被 package 中 以 from package import * 被导出的模块，即定义在__all__ 中的模块才会被 from package import * 导出。
# https://wecatch.me/blog/2016/05/28/python-module-path-find/
# import加载顺序
# sys.builtin_module_names
# sys.modules
# sys.path
# pythonpath
# 然后是python安装时设置的相关默认路径。
# logging http://huangming.work/2016-05-29-python-log.html
import random
from datetime import datetime
dt = datetime.now()

# print 直接到文件
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) #py3
# print >> f, "%3d %0.2f" % (year, principal)  #py2
with open('file.txt', 'w') as f:
    print('hello world', file=f)

# flush 刷新缓冲区
import sys,time
for i in range(30): #进度条类型 
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.2)

# glob使用
for name in glob.glob('*[0-9]*.txt'):
for name in glob.iglob('**/*.py', recursive=True):

#读文件使用
f.read().splitlines()

# 得到各个文件名称
import os
file_path = "D:/test/test.py"
(filepath,tempfilename) = os.path.split(file_path)
(filename,extension) = os.path.splitext(tempfilename)



# list 复制
random_lst = [random.random() for i in range(10)]
cpy_random_lst = random_lst[:]

# list 选择从b list中
[a[x] for x in b]

# 去除list中的空串  
list(filter(lambda s:s and s.strip(), value))

# 批量赋值满足条件的元素
def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            # 批量赋值满足条件的元素
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return primes, sum(primes)
countPrimes(100)

# python3 中dict keys() 方法返回的不是list  需要list(d.keys())
# python3 中map filter reduce 返回的是生成器
# from functools import reduce

def loopTwoList():
    list1 = [1,2,3,4] 
    list2 = [5,6,7,8] 
    for (i1, i2) in zip(list1,list2): 　　
    i3 = i1 + i2
    print(i3)

# dict转为class
# https://stackoverflow.com/questions/1305532/convert-nested-python-dict-to-object
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
def dict2Class():
    d = {'a':1, 'b': 10}
    obj = Struct(**d)
    print(obj, obj.a)

# vars(obj) 将 obj转换为字典
def class2dict():
    class A():
        pass
    a = A()
    a.a = 1
    a.b = 10
    d = vars(a)
    print(d)


# IO文件##################################################################################
# 打开文件
# datetime https://blog.csdn.net/shomy_liu/article/details/44141483
def useFile():
    with open('file1' + dt.strftime( '%Y_%m_%d_%H_%M_%S_%f' ), 'w') as f1, \
        open('file2' + dt.strftime( '%Y_%m_%d_%H_%M_%S_%f' ), 'w') as f2:
        for x,y in zip(f1.readlines(),f2.readlines()):
            print(x,y)
        f1.write('haha')
        f2.write('shii')

    with open('file1' + dt.strftime( '%Y_%m_%d_%H_%M_%S_%f' ), 'r') as f:
        lines = f.readlines()
        print(lines)
from contextlib import nested #这个包是python2中的，不使用python3
with nested(open('file1'), open('file2'), open('file3')) as (f1,f2,f3):
 for i in f1:
  j = f2.readline()
  k = f3.readline()
  print(i,j,k)
# py3
from contextlib import ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # Do something with "files"
# json
# loads/dumps 得到字符串, laod/dump 直接写入文件
# python的json.dumps方法默认会输出成这种格式"\u535a\u5ba2\u56ed",
# json.dumps({'text':"中文"},ensure_ascii=False,indent=2)

# 重新加载包
# import importlib
# importlib.reload(AugDataset)

# 字符串
# 遍历每个unicode词
str = '我是abc'
str = str.decode('utf-8')
for index in range(len(str)):
    print str[index]