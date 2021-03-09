#encoding=utf8
# https://www.cnblogs.com/gongpixin/p/6761389.html
# https://www.cnblogs.com/s1124yy/p/5818108.html
import numpy as np
def bin_search(arr, x):
    st, ed = 0, len(arr) - 1
    while st <= ed:
        m = (st + ed) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            ed = m - 1
        else:
            st = m + 1
    return -1

#在非递减数组nums中，lower_bound(nums, target)返回第一个大于等于target的值得位置，
#如果nums中元素均小于target（即不存在>=target的元素），则返回nums的长度（即target如果要插入到nums中，应该插入的位置）
def lower_bound(arr, x):
    st, ed = 0, len(arr) - 1
    pos = len(arr)
    while st <= ed:
        m = (st + ed) // 2
        if arr[m] < x:
            st = m + 1
        else:
            ed = m - 1
    return st
#返回第一个大于target的值的位置
def upper_bound(arr, x):
    st, ed = 0, len(arr) - 1
    pos = len(arr)
    while st <= ed:
        m = (st + ed) // 2
        if arr[m] <= x:
            st = m + 1
        else:
            ed = m - 1
    return st

r = bin_search([1,2,3,34,56,57,78,87],57)
print(r)

r = lower_bound([1,2,3,7,7,34,56,57,78,87],7)
print(r)

r = upper_bound([1,2,3,7,7,34,56,57,78,87],7)
print(r)




##############################################
