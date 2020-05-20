#encoding=utf8
import numpy as np

# 树状数组/st/lca

# BinaryIndexTree
LEN = 10
bitArr = [0] * LEN
def BitAdd(idx, x):
    while idx < LEN:
        bitArr[idx] += x
        idx += idx&(-idx)

def BitSum(idx):
    ret = 0
    while idx > 0:
        ret += bitArr[idx]
        idx -= idx&(-idx)
    return ret


#
arr = [1,2,10,4444,5]
for i, a in enumerate(arr, 1):
    BitAdd(i, a)
    print i,a,bitArr
print(BitSum(4))


#####################################################
class Node:
    def __init__(self, val):
        self.val = val
        self.child = []

vis = [0] * LEN
fa = [i for i in range(LEN)]
nodes = []
query = []

def find(x):
    if x == fa[x]:
        return x
    else:
        fa[x] = Find(fa[x])
        return fa[x]

def LCA(u):
    for v in nodes[u].child:
            LCA(v)
            fa[v] = u
    
    vis[u] = 1
    for v in que[u].child:
        if vis[v]:
            ans[u][v] = find(v)

mn = [[0] for i in range(LEN)]
log2 = [0] * LEN
def st():
    for i in range(LEN):
        log2[i] = -1 if i == 0 else log2[i >> 1] + 1
    for j in range(1, 20):
        for i in range(1, LEN+1):
            if (1<<j) > LEN:
                break
            mn[i][j] = min(mn[i][j - 1], mn[i + (1 << j - 1)][j - 1])

def st_query(ql, qr):
    k = log2[qr - ql + 1];
    return min(mn[ql][k], mn[qr - (1 << k) + 1][k])

def ST( n) {
    for i in range(1, n+1):
        dp[i][0] = A[i]
    for (int j = 1; (1 << j) <= n; j++) 
        for (int i = 1; i + (1 << j) - 1 <= n; i++) 
            dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);
        
    

int RMQ(int l, int r) {
    int k = 0;
    while ((1 << (k + 1)) <= r - l + 1) k++;
    return max(dp[l][k], dp[r - (1 << k) + 1][k]);
}
