import collections
# 滑动窗口实现
buffer = collections.deque(maxlen=window)

# 中文的TFIDF使用
data['cut_comment'] = data['Discuss'].apply(lambda x:' '.join(i for i in jieba.cut(x)))
tf = TfidfVectorizer(ngram_range=(1,2), analyzer='char')
discuss_tf = tf.fit_transform(data['cut_comment'])
# hash feat 使用word级别的数据
ha = HashingVectorizer(ngram_range=(1,2), lowercase=False)
discuss_ha = ha.fit_transform(data['cut_comment'])
data = hstack((discuss_tf, discuss_ha)).tocsr()
