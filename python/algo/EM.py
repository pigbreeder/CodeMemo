#! /usr/bin/env python  
#! -*- coding=utf-8 -*-  
# https://blog.csdn.net/zouxy09/article/details/8537620
# https://zhuanlan.zhihu.com/p/25799397 
# https://www.cnblogs.com/pinard/p/6912636.html
# 目标
# ΣΣ Qi(z)log(p(x,z;θ)/Q(z))
# 模拟两个正态分布的均值估计  
# θ是均值Miu，隐变量是归属于某个分布的概率Posterior
# 固定θ求Posterior隐变量z，E
# 固定Posterior求θ，M
from numpy import *  
import numpy as np  
import random  
import copy  
  
SIGMA = 6  
EPS = 0.0001  
#生成方差相同,均值不同的样本  
def generate_data():      
    Miu1 = 20  
    Miu2 = 40  
    N = 1000  
    X = mat(zeros((N,1)))  
    for i in range(N):  
        temp = random.uniform(0,1)  
        if(temp > 0.5):  
            X[i] = temp*SIGMA + Miu1  
        else:  
            X[i] = temp*SIGMA + Miu2  
    return X  
  
#EM算法  
def my_EM(X):  
    k = 2  
    N = len(X)  
    Miu = np.random.rand(k,1)  
    Posterior = mat(zeros((N,2)))  
    dominator = 0  # 分母
    numerator = 0  # 分子
    #先求后验概率  Q
    for iter in range(1000):  
        for i in range(N):  
            dominator = 0  
            for j in range(k):  
                # 得到该高斯分布的采样，样本总计来为后续计算均值打下基础
                dominator = dominator + np.exp(-1.0/(2.0*SIGMA**2) * (X[i] - Miu[j])**2)  

            for j in range(k):  
                numerator = np.exp(-1.0/(2.0*SIGMA**2) * (X[i] - Miu[j])**2)  
                Posterior[i,j] = numerator/dominator              
        oldMiu = copy.deepcopy(Miu)  
        #最大化      每个样本都有归属于某个正态分布的概率。
        for j in range(k):  
            numerator = 0  
            dominator = 0  
            for i in range(N):  
                numerator = numerator + Posterior[i,j] * X[i]  
                dominator = dominator + Posterior[i,j]  
            Miu[j] = numerator/dominator  
        print 'error:', (abs(Miu - oldMiu)).sum()   
            #print '\n'  
        if (abs(Miu - oldMiu)).sum() < EPS:  
            print Miu,iter  
            break  
  
if __name__ == '__main__':  
    X = generate_data()  
    my_EM(X)    