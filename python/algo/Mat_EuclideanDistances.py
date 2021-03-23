#encoding=uf8
# https://blog.csdn.net/frankzd/article/details/80251042
# https://blog.csdn.net/wanghai00/article/details/54021200
# 两个矩阵计算欧式距离
# MXH, NXH
# m1n1 = (m1h1-n1h1)^2 + (m1h2-n1h2)^2+ ... +(m1hn-n1hn)^2 开根号
# m1n1 = m1h1**2 + m1h2**2 ...m1hn**2 + n1h1**2 + n1h2**2 +...+n1hn**2 - -2*m1h1*n1h1 ... 2*m1hn*n1hn
# 
def EuclideanDistances(A, B):
    BT = B.transpose()
    # vecProd = A * BT
    vecProd = np.dot(A,BT)
    # print(vecProd)
    SqA =  A**2
    # print(SqA)
    sumSqA = np.matrix(np.sum(SqA, axis=1))
    sumSqAEx = np.tile(sumSqA.transpose(), (1, vecProd.shape[1]))
    # print(sumSqAEx)

    SqB = B**2
    sumSqB = np.sum(SqB, axis=1)
    sumSqBEx = np.tile(sumSqB, (vecProd.shape[0], 1))    
    SqED = sumSqBEx + sumSqAEx - 2*vecProd
    SqED[SqED<0]=0.0   
    ED = np.sqrt(SqED)
    return ED