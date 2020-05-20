# numpy

## 信息查看
```
ndarray.ndim：数组的维数 
ndarray.shape：数组每一维的大小 
ndarray.size：数组中全部元素的数量 
reshape	不改变数据的条件下修改形状
flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
ravel	返回展开数组（一维）
```
## 数据生成
```
np.arange(0, 20, 2)
np.linspace(0, 1, 5)
np.random.randint(0, 10, (3, 3))
np.zeros( (3,4) )
np.ones( (2,3,4), [dtype=np.int16])
np.empty( (2,3) ) 
生成随机正态分布数组
numpy.random.uniform(low,high,(dimension,number))
（dimension行，number列）
np.random.permutation 生成随机排列数 
np.random.choice() #赋予权值选择 多项式分布
torch.multinomial(t.tensor([0.1,0.4,0.5]), 2) #多项式分布
```

## 索引
```
x[[0,1,2],  [0,1,0]]  # 选三个数，各个轴的下标
a[...,1:] # 去除首列
a[1:3, 1:3] # 选择子矩阵
x[x >  5] #布尔索引
np.nonzero (a) #返回输入数组中非零元素的索引
######################################################
y = np.where(x >  3)  #返回输入数组中满足给定条件的元素的索引
cond = numpy.array([True,False,True,False])
a = numpy.where(cond,-2,2)# [-2  2 -2  2]
cond = numpy.array([1,2,3,4])
a = numpy.where(cond>2,-2,2)# [ 2  2 -2 -2]
b1 = numpy.array([-1,-2,-3,-4])
b2 = numpy.array([1,2,3,4])
a = numpy.where(cond>2,b1,b2) # 长度须匹配# [1,2,-3,-4]
统计数值sum(ret) or  from collections import Counter
TN = (ret[labels==0]==0).sum()
######################################################

# 1个句子，60000词表大小，做一次分解(768 128) 耗时

ori_W = np.random.randn(60000,768)
factorized_W1 = np.random.randn(600000,128)
factorized_W2 = np.random.randn(128,768)

# exp1: 
text = np.random.randint(0,60000,(1,30))
time factor_input = np.dot(factorized_W1[text] ,factorized_W2)
time ori_input = ori_W[text]

# exp2: 
text = np.random.randint(0,60000,(3,30))
time factor_input = np.dot(factorized_W1[text] ,factorized_W2)
time ori_input = ori_W[text]

```
```
# https://www.runoob.com/numpy/numpy-array-manipulation.html
A*B
np.transpose(a) = a.T # 翻转
a = np.arange(8).reshape(2,2,2) print (np.swapaxes(a, 2, 0)) # 交换数组的两个轴
## 配合使用
np.expand_dims(x, axis = 1) 函数通过在指定位置插入新的轴来扩展数组形状
numpy.squeeze 函数从给定数组的形状中删除一维的条目

concatenate	连接沿现有轴的数组序列
stack	沿着新的轴加入一系列数组。
hstack	水平堆叠序列中的数组（列方向）
vstack	竖直堆叠序列中的数组（行方向）
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> b = np.array([[10,20],[30,40],[50,60]])
np.concatenate((a,b))
array([[ 1,  2],                                                                                                                                               
       [ 3,  4],                                                                                                                                               
       [ 5,  6],                                                                                                                                               
       [10, 20],                                                                                                                                               
       [30, 40],                                                                                                                                               
       [50, 60]])
>>> np.vstack((a,b))
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [10, 20],
       [30, 40],
       [50, 60]])
>>> np.hstack((a,b))
array([[ 1,  2, 10, 20],
       [ 3,  4, 30, 40],
>>> np.stack((a,b), axis=1)
array([[[ 1,  2],
        [10, 20]],

       [[ 3,  4],
        [30, 40]],

       [[ 5,  6],
        [50, 60]]])
```
## 函数
```
# https://www.runoob.com/numpy/numpy-sort-search.html
A.dot(B)
np.partition(a, 3)  # 将数组 a 中所有元素（包括重复元素）从小到大排列，比第3小的放在前面，大的放在后面
np.partition(a, (1, 3)) # 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
np.argsort(x)  
numpy.argmax()
numpy.argmin()


## 广播的用法 从最后一维往前1或相等就行
计算两个矩阵a,b (seq,hidden)的相似度，a=a.unsqueeze(0) 先增加维度,到(1, seq, hidden)
euclidean = (torch.pow(x1 - x2.permute(1, 0, 2), 2).sum(dim=2) + eps).sqrt()
np.matmul(a, b.permute(1,0,2))

## 打乱数据
np.random.seed(2018)
index = np.arange(train.shape[0])
np.random.shuffle(index)
train_shuffle,train_y_shuffle = train.iloc[index,:],train.Score.values[index]

## 文件操作
文件存储
np.save(f_pth, nums)
pre_word = np.load('data/processed/embedding.npz.npy')
读取txt中的矩阵数据
C#的comment问题；分隔符明确\xa0
t = np.genfromtxt('sgns.wiki.bigram-char',skip_header=1,comments=None, delimiter=' ', usecols=list(range(1,301)))
```
```
判断是否为nan
np.isnan(np.exp(X)).any()
np.exp的爆炸导致inf 然后再计算就得到了nan
统计nan个数
np.isnan(arr).sum()
np.count_nonzero
np.count_nonzero(y == 1)
#比如：
a = np.array([1, np.nan, 3, 4, np.nan, 6])
Nan的个数：
print len(a[np.isnan(a)])
非Nan的个数：
print len(a[~np.isnan(a)])
获取inf数据的位置
https://stackoverflow.com/questions/37754948/how-to-get-the-indices-list-of-all-nan-value-in-numpy-array
 np.argwhere(np.isinf(dd))
布尔数组
retArray[dataMatrix[:,dimen] <= threshVal] = -1.0   
np.isin(element, test_elements)
element在不在test_中，输出是Boolean数组
没找出来的正确 data_val.iloc[one_label_[0][~np.isin(one_label_,out_label_)[0]]] #FP
找的错误的正确 data_val.iloc[out_label_[0][~np.isin(out_label_,one_label_)[0]]] #FN
np.any(a==b) 任意一个即可
np.all(a==b) 判断是否全为True
打印出所有的数值
np.set_printoptions(threshold=np.inf)
```


argpartition
是将第k大的数字，放在第k个位置。类似于快排找第k大的数，堆其它数不做排序，比较省计算。

## 自定义函数
```
ufunc：对数组每个元素进行操作
http://blog.csdn.net/taxueguilai1992/article/details/46581861
http://www.cnblogs.com/cv-pr/p/6395176.html #矩阵基本运算
广播
ufunc函数对两个数组进行计算时，ufunc函数会对这两个数组的对应元素进行计算，因此它要求这两个数组有相同的大小(shape相同)。如果两个数组的shape不同的话，会进行如下的广播(broadcasting)处理
自定义向量操作
vfunc = np.vectorize(myfunc) vfunc([1, 2, 3, 4], 2)
np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 5)
array([[ 0, 1, 2, 3, 4],
     [10, 11, 12, 13, 14],
     [20, 21, 22, 23, 24],
     [30, 31, 32, 33, 34],
     [40, 41, 42, 43, 44],
     [50, 51, 52, 53, 54]])
对每个元素进行操作
def f(x):
    return 0 if x<0.5 else 1
f = np.vectorize(f)
ret = f(outs)



arr.sum(axis=None) 这个是标明哪个维度相加，默认全相加。axis=0，第0维全部相加.
eg:array([[1, 2, 3],
       [4, 5, 6]])  --->array([6,15])
argsort函数返回的是数组值从小到大的索引值
tile 重复多次，一般用来将向量转为矩阵，以用来和训练数据运算使用。np.tile(arr,(d2,d1,d0)) 相当于重复的维度倒着来看
operator.itemgetter 获取对象某个维的数据 http://blog.csdn.net/dongtingzhizi/article/details/12068205
squeeze 压缩维度为1的numpy向量
argmax 获取最大值的下标
permute  维度换位
swapaxes 交换两个轴
```