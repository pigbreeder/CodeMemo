#encoding=utf8
# https://blog.csdn.net/lyhvoyage/article/details/8545852  # 二进制压缩 01背包
# https://www.cnblogs.com/anzhengyu/p/11408466.html
def knapsack_01(weighs, values, pack_weight):
    arr = [0] * (pack_weight + 1)
    for w, v in zip(weighs, values):
        for idx in range(pack_weight, w, -1):
            arr[idx] = max(arr[idx], arr[idx - w] + v)
    return arr[pack_weight]
# arr[w] arr[2*w] arr[3*w] 遍历顺序
def knapsack_complete(weighs, values, pack_weight):
    arr = [0] * (pack_weight + 1)
    for w, v in zip(weighs, values):
        for idx in range(w, pack_weight+1):
            arr[idx] = max(arr[idx], arr[idx - w] + v)
    return arr[pack_weight]
def knapsack_multiple(weighs, values, nums, pack_weight):
    arr = [0] * (pack_weight + 1)
    for i,(w, v) in enumerate(zip(weighs, values)):
        for idx in range(pack_weight, w, -1):
            for num in range(nums[i]):
                if w*num > pack_weight:
                    break
                arr[idx] = max(arr[idx], arr[idx - w*num] + v*num)
    return arr[pack_weight]
weights = [77,22,29,50,99]
values = [92,22,87,46,90]
weight = 100
r = knapsack_01(weights,values,weight)
print(r)
r = knapsack_multiple(weights,values,[1,2,1,2,3],weight)
print(r)
r = knapsack_complete(weights,values,weight)
print(r)
# out 133
weights = [79,58,86,11,28,62,15,68]
values = [83,14,54,79,72,52,48,62]
weight = 200
# out 334
r = knapsack_01(weights,values,weight)
print(r)

##############################################
# LIS
def getLIS(self, A, n):
    L = [1]*n
    for cur,val in enumerate(A):
        for pre in range(cur):
            if A[pre]<=A[cur]:
                L[cur] = max(L[cur],1 + L[pre])

    return max(L)
# LCS
def LCS(s1, s2):
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    dp = [[0] * l2 for i in range(l1)] 
    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i - 1][j] if dp[i - 1][j] > dp[i][j - 1] else dp[i][j - 1]
    return dp[l1-1][l2-1]

A="1A2C3D4B56"
B="B1D23CA45B6A"
# 12C4B6 or 123456
print('LCS=', LCS(A,B))
################################################
# interval 中间点 dp
# https://blog.csdn.net/qq_36387683/article/details/79924574
def matrix_chain(arr):
    ll = len(arr)
    # 错误初始化
    #dp = [[0] * ll] * ll
    dp = [[0] * ll for i in range(ll)]
    for l in range(2, ll):
        for st in range(ll):
            ed = st + l -1 # 连乘中的最后一个
            if ed >= ll-1: break
            dp[st][ed] = 100000
            # 在第一个与最后一个之间寻找最合适的断开点
            # 这是从st开始，即要先计算两个单独矩阵相乘的乘次
            for k in range(st, ed):
                tmp = arr[st]*arr[k+1]*arr[ed+1] + dp[st][k] + dp[k+1][ed]
                #print(st,ed,k,tmp)
                dp[st][ed] = min(dp[st][ed],tmp)
            #print(ll,st,ed,dp[st][ed])
    #print(dp)
    return dp[0][ll-2]
arr=[3,2, 2,5, 5,10, 10,2, 2,3]
arr=[30, 35, 15,5,10,20,25]
arr=[3,2, 2]
print('matrix_chain=', matrix_chain(arr))



# 股票买卖最佳时机
# https://blog.csdn.net/qq_35865125/article/details/89818929

# 最优二叉搜索树
# 二维矩阵枚举中间点,边界为0
# https://zhuanlan.zhihu.com/p/54171342
# https://blog.csdn.net/zhang_xiaomeng/article/details/72820147



# 剪绳子
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-huan-s-xopj/
# dp[2] = 1
# dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]