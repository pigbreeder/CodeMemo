#encoding=utf8
# heap 
# https://blog.csdn.net/leex_brave/article/details/51490647
# https://blog.csdn.net/IqqIqqIqqIqq/article/details/52742377
# qsort
# https://www.cnblogs.com/TenosDoIt/p/3665038.html
import numpy as np
def merge_sort(arr, st, ed):
    if st >= ed:
        return
    m = (st + ed) // 2
    merge_sort(arr, st, m)
    merge_sort(arr, m+1, ed)
    tmp = [0] * len(arr)
    i1, i2 = st, m+1
    k = st
    while i1 <= m and i2 <= ed:
        if arr[i1] < arr[i2]:
            tmp[k] = arr[i1]
            i1 += 1
        else:
            tmp[k] = arr[i2]
            i2 += 1
        k += 1
    while i1 <= m:
        tmp[k] = arr[i1]
        i1 += 1
        k += 1
    while i2 <= ed:
        tmp[k] = arr[i2]
        i2 += 1
        k += 1
    while st<=ed:
        arr[st] = tmp[st]
        st += 1
    return arr
# 堆结构本身调整，删除就换到最后一位然后下调，增加就追加到后面然后上调
def heap_adjust(arr, st, ed):
    # 从根调整,下调
    root = st
    while True: 
        child = 2 * root + 1
        if child > ed:
            break
        # 找到孩子中的最大
        if child + 1 <= ed and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
def head_sort(arr):
    first = len(arr) // 2 - 1
    # 从倒数第二层调整堆
    for st in range(first, -1, -1):
        heap_adjust(arr, st, len(arr) - 1)
    # 已经构建成了堆，然后对于新元素插入调整
    for ed in range(len(arr) - 1, 0, -1):
        arr[0], arr[ed] = arr[ed], arr[0]
        heap_adjust(arr, 0, ed - 1)
    return arr
def qsort(arr,st,ed):
    if st >= ed:
        return
    #m = partition1(arr, st, ed)
    m = partition2(arr, st, ed)
    qsort(arr, st,m -1)
    qsort(arr, m+1, ed)
    return arr

def partition2(arr, l, h):
    pivot = arr[l]
    while l < h:
        while arr[h] >= pivot and h > l:
           h -= 1 
        arr[l] = arr[h] 
        while arr[l] <= pivot and h > l:
           l += 1 
        arr[h] = arr[l] 
    arr[l] = pivot
    return l

def partition1(arr, st, ed):
    pivot = arr[st]
    loc = st # loc 总保证是小于pivot的数字位置,+1位置是可以置换的位置
    for i in range(st,ed+1):
        if arr[i] < pivot:
            loc += 1
            arr[i], arr[loc] = arr[loc], arr[i]
    arr[st], arr[loc] = arr[loc], arr[st]
    return loc

arr = np.random.randint(100,size=5)
st = 0
ed = len(arr)- 1
print('arr=',arr)
arr2 = qsort(arr[:],st,ed)
print('qsort=',arr2)
arr2 = merge_sort(arr[:],st,ed)
print('merge=',arr2)
arr2 = head_sort(arr[:])
print('head_sort=',arr2)
