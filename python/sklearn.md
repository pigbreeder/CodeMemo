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

# 数据查看
df.isnull().any() #拿到数据先看每列是否为空
# 查看缺失值
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
# 查看缺失值是谁
df[df['c1']==None]
cond=df[(df['列名1']>‘列值1’)&(df['列名1']<‘列值2’)]
去除null和空串
tst_df[((tst_df['sentence'].isnull())\
	| (tst_df['sentence'].str.replace(' ','') == ''))]
filtered_df = df[df['name'].notnull()]


# 数据排序
all_df = all_df.sort_values(['index'])

# 数据访问

columns:df['label']
rows:df[idx1:idx2]
# 指定行赋值，loc而不是iloc         
df.loc[tst_df.index,'reject_score'] 
# 行是index，列是name
df.loc[df.index[#], 'NAME'] where # is a valid integer index and NAME is the name of the column.

# 最大的前三
df.nlargest(3, 'population')
df.sort_values(['job','count'],ascending=False).groupby('job').head(3) # group
df.groupby(["name"])["count_1"].nlargest(3)

cells: 
df.iloc[idx,idx_col], df.loc[idx_name,idx_name_col]

df.select_dtypes(exclude=['int64']) # 按照类型选取

# pandas 加载数据None，字符串为空等情况
to_csv(keep_default_na=False, encoding='utf-8_sig') # 如果用excel打开是乱码则这样encoding，读取excel用gb2312

# 新生成一列，用split
df[['top1_name', 'top1_score']] = out_df.iloc[:,0].str.split(':',1,expand=True)

# 遍历
for i, row in colTypes.iterrows():
.iterrows() # 更快

# 连续变离散 cut
np.random.seed(666)  #让结果可重复
ser = pd.Series(np.random.random(20))
print(ser.head())

pd.qcut(ser,
    q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
    labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th','10th'])

# qcut 按照数量均分到各个桶
# cut 按照range均分 很直观
# https://zhuanlan.zhihu.com/p/68194655
factors = np.random.randn(30)
pd.qcut(factors, 5).value_counts()
pd.cut(factors, 5).value_counts()


pd series连接
pd.concat([s1, s2], axis=1).reset_index()
按照index排序
sort_index
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sum.html
# 理解多层index的筛选方式

# 集合运算
交集
intersected_df = pd.merge(df1, df2, how='inner')
并集
intersected_df = pd.merge(df1, df2, how='outer')
指定列
取并集：print(pd.merge(df1,df2,on=['name', 'age', 'sex'], how='outer'))
差集
set_diff_df = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)

# series调换index和value
https://stackoverflow.com/questions/40146472/quickest-way-to-swap-index-with-values
print(pd.Series(s.index.values, index=s ))


# 去重
dframe.duplicated() # 检测重复行
dframe.drop_duplicates()  # 丢弃行
dframe.drop_duplicates('color') # 根据字段去重
可以找到具有unique = df [df.duplicated()]的所有唯一行,
然后使用unique.iterrows()迭代唯一条目,并在pd.where()的帮助下提取相等条目的索引

# pd 注意设置值的方式
df.iloc[filter_condition,'loc_name'] = set_value 👌
df.iloc[filter_condition]['loc_name'] = set_value 😂
筛选后连接，reset_index 不然连接有问题
# 注意链式分配
df[df.A == 0]['B'] = 10 # 错误用法
df1 = [df.A == 0];df1.loc[0, 'B'] = 10 # 错误用法，错误引用
df[df.A == 0, 'B'] = 10 # right
https://zhuanlan.zhihu.com/p/40874154


# 划分测试集
train_data = dataset.sample(frac=0.95,random_state=0,axis=0)
other_data = dataset[~dataset.index.isin(train_data.index)]
dev_data = other_data.sample(frac=0.5,random_state=0,axis=0)
test_data = other_data[~other_data.index.isin(dev_data.index)]
alias scpme='_a(){ scp xsy@ip_address:${1} $2;}; _a'

----------------------------------------------------------------------------------------

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





# 绘图相关

https://www.cnblogs.com/Cheryol/p/13513871.html
https://blog.csdn.net/qq_18668137/article/details/103766163 # 绘图时x轴标签重叠的解决办法
df_sex.plot(kind='bar',stacked = True,figsize=(20,10))

histogram的横坐标是连续变量，将连续变量分成固定的组，组别之间是固定不变的。例如:
横坐标：1-10, 11-20, 21-30, 31-40. (横坐标无法改变顺序)
纵坐标：每组的频次 或者 比例
bar chart的横坐标为分类变量，例如：
横坐标：去学校的各种交通方式，走路，骑车，打车，开车 （横坐标无先后顺序 可自由调整）
纵坐标：每种交通方式的频次 或者 比例

```