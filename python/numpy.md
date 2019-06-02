# numpy
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

## 数据选择统计
选择需要的数据，索引坐标 查找
# 先选出需要判断的位置，再选出需要得数值，最后统计
https://ask.sagemath.org/question/10279/frequency-count-in-numpy-array/
统计数值sum(ret) or  from collections import Counter
TN = (ret[labels==0]==0).sum()
np.where 得到具体的位置坐标列表

注意每个计算时的坐标是当前数据的坐标还是坐标数组内容
label[label==1] 这个取出来的是一个新数组，在这个基础上再操作坐标就对应不到原有的数组了
axis=np.where(label==1) 先拿到坐标，在对应查看,若要后续操作，
axis2=axis[np.where(la2[axis]==0)],取出原有坐标数组中的内容作为坐标存起来


np.all

numpy.unique
Find the unique elements of an array.

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



argpartition
是将第k大的数字，放在第k个位置。类似于快排找第k大的数，堆其它数不做排序，比较省计算。

## 数据生成
生成随机正态分布数组
numpy.random.uniform(low,high,(dimension,number))
（dimension行，number列）
np.random.permutation 生成随机排列数 
np.random.choice() #赋予权值选择 多项式分布
torch.multinomial(t.tensor([0.1,0.4,0.5]), 2) #多项式分布

创建空数据
>>> a = numpy.empty((0,2),int)
>>> a = numpy.append(a, [[1, 2]], axis=0)
>>> a = numpy.append(a, [[8, 8]], axis=0)
array([[ 1,  2],
       [ 8,  8]])
使用索引时，注意逗号的使用，标明是维度的分割。
结构数组：和C的struct互通
a = np.array([[0,1,2],[3,4,5],[6,7,8]], dtype=np.float32)


## 自定义函数
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
