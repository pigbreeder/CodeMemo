# coding=utf-8
from __future__ import print_function
def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

def heapify(arr, n, i):
    # 构建大顶堆
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # 构建大顶堆
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # 一个个交换元素
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
    return arr

# 归并排序
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
  
    # 拷贝数据到临时数组 arrays L[] 和 R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # 归并临时数组到 arr[l..r] 
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = l     # 初始归并子数组的索引
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # 拷贝 L[] 的保留元素
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # 拷贝 R[] 的保留元素
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def merge_sort(arr,l,r): 
    if l < r:    
        m = int((l+(r-1))/2)
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r) 
    return arr
  
# 二分查找
def binary_search (arr, l, r, x): 
  
    # 基本判断
    if r >= l:  
        mid = int(l + (r - l)/2)
  
        # 元素整好的中间位置
        if arr[mid] == x: 
            return mid 
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x: 
            return binary_search(arr, l, mid-1, x) 
  
        # 元素大于中间位置的元素，只需要再比较右边的元素
        else: 
            return binary_search(arr, mid+1, r, x) 
    else: 
        # 不存在
        return -1
if __name__=="__main__":
    import copy
    lists=[30,24,5,58,18,36,12,42,39]
    heap_list = copy.deepcopy(lists)
    merge_list = copy.deepcopy(lists)
    print("排序前的序列为：")
    for i in lists:
        print(i,end=" ")
    print("\nquick_sort排序后的序列为：")
    for i in quick_sort(lists,0,len(lists)-1):
        print(i,end=" ")
    print("\nheap_sort排序后的序列为：")
    for i in heap_sort(heap_list):
        print(i,end=" ")
    print("\nmerge_sort排序后的序列为：")
    for i in merge_sort(merge_list,0,len(lists)-1):
        print(i,end=" ")
    print("\n binary_search 39:",binary_search(merge_list,0,len(lists)-1,39))

#排序前的序列为：
#30 24 5 58 18 36 12 42 39
#排序后的序列为：
#5 12 18 24 30 36 39 42 58#