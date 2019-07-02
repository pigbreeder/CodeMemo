#补全长度 #
seq[i] = seq[i] + 'P' * (n_step - len(seq[i]))
#对应位置赋值为1（one-hot编码） #
np.eye(n_class)[input]
#四位对齐
string += '=' * (-len(string) % 4) 

# NLP预处理
test_sentence = """When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty\\'s field.""".split()

vocb = set(test_sentence) # 通过set将重复的单词去掉
word_to_idx = {word: i for i, word in enumerate(vocb)}
idx_to_word = {word_to_idx[word]: word for word in word_to_idx}

trigram = [((test_sentence[i], test_sentence[i-1]), test_sentence[i-2])
           for i in range(len(test_sentence)-2)]

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