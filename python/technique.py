
# flush 刷新缓冲区 为了写文件中途出问题终止浪费调用
import sys,time
for i in range(30): #进度条类型 
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.2)

# glob使用
for name in glob.glob('*[0-9]*.txt'):
for name in glob.iglob('**/*.py', recursive=True):
    print(name)

# zip 和 unzip 
import numpy as np
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
zz=zip(a,b,c)
print(zz)

x,y,z=zip(*zz)
print(x)
print(y)
print(z)

输出：
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)



# 得到符合的数据下标
filter_idx = list(filter(lambda x: words[x] in dict_table, range(len(words))))
# 从列表中挑选(如果是numpy则直接data[filter_idx]。字典智能挨个找，numpy也没用
# print 中逗号会输出空格。要注意
prob = [dict_table[words[i]][1] for i in filter_idx]
#补全长度 #
seq[i] = seq[i] + 'P' * (n_step - len(seq[i]))
#对应位置赋值为1（one-hot编码） #
np.eye(n_class)[input]
#四位对齐
string += '=' * (-len(string) % 4) 

# choices归一化
p = np.array(p)
filter_idx = np.random.choice(filter_idx, 2 if np.random.rand()> 0.5 else 1, False,p/p.sum())

# 显示进度条
import mmap
def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines
for idx, line in enumerate(tqdm(fi, total=get_num_lines(input_file)), 1):
	pass

# NLP预处理
test_sentence = """When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty\\'s field.""".split()

vocb = set(test_sentence) # 通过set将重复的单词去掉
word_to_idx = {word: i for i, word in enumerate(vocb)}
idx_to_word = {word_to_idx[word]: word for word in word_to_idx}

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

#BPE
#先拆分最早结合的词是因为先合并先拆开更能看到剩余的新词
#如果按照后面词合并，max的操作则导致后面凝聚度很高的先出现了
self.bpe_codes = [tuple(item.split()) for item in codes]
# 去重，仅保留第一个出现的位置
self.bpe_codes = dict([(code,i) for (i,code) in reversed(list(enumerate(self.bpe_codes)))])
# tuple把每个单词都拆掉
word = tuple(orig[:-1]) + ( orig[-1] + '</w>',)



#Mask矩阵应用
#https://www.zhihu.com/question/305508138
def subsequent_mask(size):
    "Mask out subsequent positions."
    attn_shape = (1, size, size)
    subsequent_mask = np.triu(np.ones(attn_shape), k=1).astype('uint8')
    return torch.from_numpy(subsequent_mask) == 0

# 字符判断
# https://zhuanlan.zhihu.com/p/84625185 语言检查
# https://www.168seo.cn/python/1993.html