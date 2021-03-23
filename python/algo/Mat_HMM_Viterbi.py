import numpy as np
'''
https://blog.csdn.net/qq_37098526/article/details/89144282
N为隐藏状态数目
M为观测符号数目
A为状态转移矩阵：N×N
B为观测矩阵：N×M
pi为初始向量：1×N
T为观测序列长度
O为观测序列
'''
def Viterbi(M, N, A, B, pi, T, O):
    delta = np.zeros(shape=(T, N))  # delta为局部概率，即到达某个特殊的中间状态时的概率
    psi = np.zeros(shape=(T, N))  # psi为反向指针，指向最优的引发当前状态的前一时刻的某个状态
    
    # 初始化，计算初始时刻所有状态的局部概率，反向指针均为0
    # delta[0] = pi * B[:, O[1]-1]
    for i in range(N):
        delta[0][i] = pi[i] * B[i][O[0]-1]
        psi[0][i] = 0
    
    # 递推，递归计算除初始时刻外每个时间点的局部概率和反向指针
    for t in range(1, T):
        for i in range(N):
            val = delta[t-1] * A[:, i]  
            # 计算t-1时刻每个状态的局部概率与到t时刻第i个状态的转移概率之积
            maxval = max(val)  
            # 从t-1时刻到t时刻第i个状态的最大概率
            maxvalind = np.argmax(val)  
            # 使从t-1时刻到t时刻第i个状态的概率为最大的t-1时刻的状态序号
            delta[t][i] = maxval * B[i][O[t]-1]  
            # t时刻第j个状态的局部概率
            psi[t][i] = maxvalind  
            # t时刻第i个状态的反向指针
            
    # 终止，观测序列的概率等于T时刻的局部概率
    P = max(delta[T-1])
    I = [0] * T  # q记录找出的隐藏状态路径
    I[T-1] = np.argmax(delta[T-1]) + 1  # T时刻的隐藏状态
    
    # 最优路径回溯
    for t in range(T-2, -1, -1):  # 回溯记录T-1时刻到起始(1)时刻的隐藏状态路径
        I[t] = int(psi[t+1][I[t+1]-1] + 1)  # 由t+1时刻的隐藏状态及其反向指针找到t时刻的隐藏状态，+1是为了输出状态序号1~3，而不是0~2
        
    return I, P, delta

# 区别是过程中存储路径 65Line
def Viterbi2(M, N, A, B, pi, T, O):
    delta = np.zeros(shape=(T, N))  # delta为局部概率，即到达某个特殊的中间状态时的概率
    path = {}  # psi为反向指针，指向最优的引发当前状态的前一时刻的某个状态
 
    # 初始化，计算初始时刻所有状态的局部概率，反向指针均为0
    # delta[0] = pi * B[:, O[1]-1]
    for i in range(N):
        delta[0][i] = pi[i] * B[i][O[0] - 1]
        path[i] = [i]
 
    # 递推，递归计算除初始时刻外每个时间点的局部概率和反向指针
    for t in range(1, T):
        newpath = {}
        for i in range(N):
            maxval, ind = max([(delta[t - 1][j] * A[j][i], j) for j in range(N)])
            # 找到从t-1时刻到t时刻第i个状态的最大概率和使从t-1时刻到t时刻第i个状态的概率为最大的t-1时刻的状态序号
            delta[t][i] = maxval * B[i][O[t] - 1]  # 更新局部概率
            newpath[i] = path[ind] + [i]  # 更新t时刻状态i的最优路径
        path = newpath
 
    # 终止，观测序列的概率等于T时刻的局部概率
    P, last = max([(delta[T - 1][i], i) for i in range(N)])  # 输出最优概率和第T时刻哪个状态(last)达到最优概率
    path[last] = [path[last][i] + 1 for i in range(N)]  # 输出T时刻状态last的最优路径，+1是为了输出状态序号1~3，而不是0~2
 
    return path[last], P, delta
M = 2
N = 3
A = np.array([[0.5, 0.2, 0.3],
             [0.3, 0.5, 0.2],
             [0.2, 0.3, 0.5]])
B = np.array([[0.5, 0.5],
             [0.4, 0.6],
             [0.7, 0.3]])
pi = np.array([0.2, 0.4, 0.4])
T = 3
O = [1, 2, 1]

q, p, delta = Viterbi(M, N, A, B, pi, T, O)
print("最优状态序列：", q)
print("最优路径概率：", p)
print("局部概率矩阵：", delta)