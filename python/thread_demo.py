#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# 并行运算方面因为GIL（Global Interpreter Lock，全局解释器锁）
# Python的原始解释器CPython中存在着GIL，因此在解释执行Python代码时，会产生互斥锁来限制线程对å±享资源的访问，
# 直到解释器遇到I/O操作或者操作次数达到一定数目时才会释放GIL，一个进程内同一时间只能允许一个线程进行运算
# 
# 执行阻塞型I/O操作的函数，在等待系统返回结果时都会释放GIL
# Python 标准库中所有阻塞型I/O函数都会释放GIL，允许其他线程运行。time.sleep()函数也会释放GIL。

# 多线程：I/O操作多应该考虑，像网络请求爬虫一类的就应该使用多线程；
# 多进程：而cpu密集型任务，比如浮点运算和分词之类应该使用多进程来最大化利用cpu.绕开GIL
# 
import os, time, random
import logging
logging.basicConfig()
from threading import currentThread
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# submit(fn, *args, **kwargs)
# return Future object
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

def print_hello(n):
    print("I'm number {} say hello in pid {}".format(n, os.getpid()))


# map(func, *iterables, timeout=None, chunksize=1)
with ProcessPoolExecutor(max_workers=10) as executor:
    executor.map(print_hello, range(10))

def task(n):
    print('%s is running' %os.getpid())
    time.sleep(2)
    return n**2
def post_task(future):
    print('post_task %s is running' %os.getpid())
    res=future.result()  #res.result()拿到的才是对应的结果
    print('%s:<%s> parse [%s]' %(currentThread().getName(),os.getpid(),res))

def submit_demo():
    start = time.time()
    with ProcessPoolExecutor() as p:   #类似打开文件,可省去.shutdown()
        future_tasks = [p.submit(task, i) for i in range(10)]
    print('=' * 30)
    print([(idx,obj.result()) for idx,obj in enumerate(future_tasks)])
    print(time.time() - start)

    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as p:   #类似打开文件,可省去.shutdown()
        future_tasks = [p.submit(task, i) for i in range(10)]
        future_tasks_post = [p.submit(task, i).add_done_callback(post_task) for i in range(10)]
    print('=' * 30)
    print(future_tasks_post)
    #print([obj.result() for obj in future_tasks])
    print(time.time() - start)
    return future_tasks

def map_demo():
    p=ThreadPoolExecutor()
    start = time.time()
    obj=p.map(task,range(10))
    p.shutdown()
    print('='*30)
    print(list(obj))
    print(time.time() - start)
if __name__ == '__main__':
    map_demo()
    future_tasks = submit_demo()
    print('st sleep')
    time.sleep(1)
    print([obj.result() for obj in future_tasks])
