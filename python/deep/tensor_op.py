
# https://zhuanlan.zhihu.com/p/36233589
# 
torch.cat(seq,dim=0,out=None) 
# 沿着dim连接seq中的tensor, 所有的tensor必须有相同的size或为empty， 其相反的操作为 torch.split() 和torch.chunk()
torch.stack(seq, dim=0, out=None) #同上
#注: .cat 和 .stack的区别在于 cat会增加现有维度的值,可以理解为续接，stack会新加增加一个维度，可以理解为叠加

# 直接增加维度的方式 
tensorA[:,:0:0] 选取但是保持维度
tensorA[:,:None] == tensorA.unsqueeze(2)

# masked_select, the shape of mask is equal to tensor.
a = torch.Tensor([[4,5,7], [3,9,8],[2,3,4]])
b = torch.Tensor([[1,1,0], [0,0,1],[1,0,1]]).type(torch.ByteTensor)
c = torch.masked_select(a,b)

# gather的用法
遍历一遍另一个维度，过程中选取对应位置上的值。

1. 选择的dim，则遍历的时候不遍历这个dim，只是对于index中的数字起到选择作用。
2. 除了dim外，其他维度要一致。(b,l,h) 从2维度选择，则index。shape=b，l，whatever
3 考虑模拟的时候，除了dim以外循环
4 想消掉哪个维度就选择哪个维度选择，因为只有这个维度的个数能选择 

常用1 一般都是取dim=1的情况，选取对应位置词的embedding
h_masked = torch.gather(h, 1, masked_pos) #pos是对应被mask的位置下标
常用2 消除掉hidden维度
logp_target_tokens = torch.gather(logp, -1, target[..., None])[..., 0]  # [batch_size, max_len]

b = torch.Tensor([[1,2,3],[4,5,6]])
print(b)
index_1 = torch.LongTensor([[0,1],[2,0]])
index_2 = torch.LongTensor([[0,1,1],[0,0,0]])
print(torch.gather(b, dim=1, index=index_1))
print(torch.gather(b, dim=0, index=index_2))

 1  2  3
 4  5  6
[torch.FloatTensor of size 2x3]

 1  2
 6  4
[torch.FloatTensor of size 2x2]

 1  5  6
 1  2  3
[torch.FloatTensor of size 2x3]

import torch as t
# https://discuss.pytorch.org/t/how-to-select-element-in-pytorch-like-numpy/4432
# https://www.jb51.net/article/167924.htm
a = t.arange(12).reshape(2,2,3)
a
a.transpose(0,1)
a.transpose(1,2)
index_1=t.LongTensor([ [ [0,0,0],[1,1,1] ], [ [0,0,0],[0,0,0] ]])
t.gather(a,0,index_1)

# 利用broadcast得到两两相乘的结果
# 
# one hot型的矩阵相乘，就像是相当于查表，于是它直接用查表作为操作，
labels1 = K.expand_dims(labels[:, :-1], 3) # 标签(b, 到结束前一步, tag_num,1)
labels2 = K.expand_dims(labels[:, 1:], 2)  # 标签(b, 从第一步开始, 1, tag_num)
labels = labels1 * labels2 # 两个错位labels，负责从转移矩阵中抽取目标转移得分   (b,len-1,tag_num,tag_num)  每一步从哪个tag转移到另一个tag
states = K.expand_dims(states[0], 2) # (batch_size, output_dim, 1)
trans = K.expand_dims(self.trans, 0) # (1, output_dim, output_dim)
output = K.logsumexp(states+trans, 1) # (batch_size, output_dim)

states = K.expand_dims(states[0], 2) # (batch_size, output_dim, 1)
trans = K.expand_dims(self.trans, 0) # (1, output_dim, output_dim)
output = K.logsumexp(states+trans, 1) # (batch_size, output_dim)
# 这里为什么要expand_dims？
# states是batch的，先让trans 扩展一个batch维度。states扩展最后的output_dim是因为要加上转移矩阵各个位置，这样用了broadcast就能解决这个问题
# output 是转移后的结果，加上input相当于Z(各个步骤的和)
# 对数加法，exp() 这种矩阵本身的转移方式就是用加法来做。 states+trans事实上就是说“把矩阵任意两个数相乘，然后放在那里”（相当于张量的笛卡尔积）logsumexp 所以用加法，因为加完以后是exp指数相当于乘法
