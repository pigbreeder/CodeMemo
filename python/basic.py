#!/usr/bin/env python
# encoding: utf-8
import random
from datetime import datetime
dt = datetime.now()
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
        f1.write('haha')
        f2.write('shii')

    with open('file1' + dt.strftime( '%Y_%m_%d_%H_%M_%S_%f' ), 'r') as f:
        lines = f.readlines()
        print(lines)
# json
# loads/dumps 得到字符串, laod/dump 直接写入文件
# python的json.dumps方法默认会输出成这种格式"\u535a\u5ba2\u56ed",
# json.dumps({'text':"中文"},ensure_ascii=False,indent=2)

# 重新加载包
# import importlib
# importlib.reload(AugDataset)
