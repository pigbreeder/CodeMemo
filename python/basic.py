#!/usr/bin/env python
# encoding: utf-8
import random

# list 复制
random_lst = [random.random() for i in range(10)]
cpy_random_lst = random_lst[:]

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
