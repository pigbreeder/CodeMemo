#!/usr/bin/env python
# encoding: utf-8
# python shell
# 最简单：
import os
os.system('top')
os.system('cat /proc/cpuinfo')
# 想要返回值 return_code, output = subprocess.getstatusoutput(cmd)

# 判断文件
os.path.isfile("test-data")
os.path.isdir('20190520.csv')