# pandas

#25个技巧
https://blog.csdn.net/jclian91/article/details/104294475 
```
# 最基本查看
df.info()
df.describe()
import pandas_profiling
pandas_profiling.ProfileReport(df)

# 数据分布（是否归一化），分成bin
df.dtypes.value_counts(normalize=True)
# 查看集合
df["name"].unique()

# 查看缺失值
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
# 查看缺失值是谁
df[df['c1']==None]
cond=df[(df['列名1']>‘列值1’)&(df['列名1']<‘列值2’)]
# 最大的前三
movies[movies.genre.isin(counts.nlargest(3).index)].head()




# 数据访问

columns:df['label']
rows:df[idx1:idx2]

cells: 
df.iloc[idx,idx_col], df.loc[idx_name,idx_name_col], df.iax[i,j]


# pandas 加载数据None，字符串为空等情况
to_csv(keep_default_na=False)

# 遍历
for i, row in colTypes.iterrows():

# 连续变离散 cut
np.random.seed(666)  #让结果可重复
ser = pd.Series(np.random.random(20))
print(ser.head())

pd.qcut(ser,
    q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
    labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th','10th'])




# 混淆矩阵
from sklearn.metrics import confusion_matrix
y_true=[2,1,0,1,2,0]
y_pred=[2,0,0,1,2,1]
C=confusion_matrix(y_true, y_pred)

(i,j) i是gt，j是predict。横着看是召回，纵着看是准确。
df[given_labels] 看指定的label 准确，df.loc[label] recall


# 热度图，
# https://zhuanlan.zhihu.com/p/35494575
# 现实方块和内部数字，fmt不使用科学计数法，robust : 如果“Ture”和“ vmin或” vmax不存在，则使用强分位数计算颜色映射范围，而不是极值。
sns.heatmap(data, square=True, annot=True, fmt='.20g',robust=True)
```