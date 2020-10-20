# https://www.kesci.com/home/project/59e77a636d213335f38daec2
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


# read_csv
# https://www.jianshu.com/p/a2e4a5d8b139
from io import StringIO
data = ('a,b,c\n'
        '1,2,3\n'
        '4,5,6\n'
        '7,8,9')
pd.read_csv(StringIO(data))
pd.read_csv(StringIO(data),names=['foo','bar','baz'],header=0)
# out:
#     foo bar baz
# 0   1   2   3
# 1   4   5   6
# 2   7   8   9
pd.read_csv(StringIO(data),names=['foo','bar','baz'],header=None) 
# out:
#     foo bar baz
# 0   a   b   c
# 1   1   2   3
# 2   4   5   6
# 3   7   8   9

# pandas filter
# https://www.jianshu.com/p/30254bc9fb40
df = pd.DataFrame({'A':[100, 200, 300, 400, 500], \
                    'B':['a', 'b', 'c', 'd', 'e'],
                     'C':[1, 2, 3, 4, 5]})
num = [100, 200, 300]
df[df.A.isin(num)]
# 多条件筛选的时候，必须加括号'()'。
df[(df.A==100)&(df.B=='a')]
df[(df.A==100)|(df.B=='b')]



df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
 
df.filter(items=['one', 'three'])
 
#select columns by regular expression
df.filter(regex='e$', axis=1)
 
# select rows containing 'bbi'
df.filter(like='bbi', axis=0)


# 定位
# iloc就是根据索引定位
# loc就是根据标签的名称定位

dates = pd.date_range(start='20191227',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[2,2] = 1111
df.loc['20191228','B'] = 2222
#df.loc[3,'B'] = 2222  如果index是数字直接这样也行

# 排序
# https://www.cnblogs.com/loubin/p/11297681.html
df = pd.DataFrame({'b':[1,2,3,2],'a':[4,3,2,1],'c':[1,3,8,2]},index=[2,0,1,3]) 
df.sort_values(by=['b','a'],axis=0,ascending=[False,True]) 
df.sort_values(by=[3,0],axis=1,ascending=[True,False])
df.sort_index() #默认按“行标签”升序排序，或df.sort_index(axis=0, ascending=True)
df.sort_index(axis=1) #按“列标签”升序排序

# value_counts() 
# value_counts()是一种查看表格某列中有多少个不同值的快捷方法，并计算每个不同值有在该列中有多少重复值。
# 聚合 groupby agg
# https://blog.csdn.net/guoyang768/article/details/86174960
# 
# 可视化
# 直方图hist 密度图 plot(kind='kde')
# https://blog.csdn.net/sinat_35930259/article/details/80005997
import matplotlib.pyplot as plt
%matplotlib inline