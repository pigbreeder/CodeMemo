#encoding=uf8
def softmax(x):
    return np.exp(x)/np.sum(np.exp(x),axis=0)

a=np.arange(12).reshape(2, 2, 3) # batch=2,length=2,hidden=3的H
b=np.sum(a, axis=0)/a.shape[1] # sum batch
c=np.tile(b,(a.shape[1], 1, 1)) # 扩展一下
d=np.concatenate((a, c), axis=-1) # 准备attention
W=np.random.rand(6,3)
e=np.tanh(np.dot(d,W)) # 神经网络
ai=softmax(e) # 得到结果
#cp=np.dot(ai,a.transpose((0,2,1))) 
cp = ai*a # 得到 context vector

Wattn=np.random.rand(6,3) # hidden_size 是词表大小
Pwe=softmax(np.dot(np.concatenate((a,cp),axis=-1), Wattn))
idx=np.random.randint(3,size=(2,2)) # 两个长度为2的句子用的词
#em=np.zeros((4,3))
#em[np.arange(4),idx.reshape(-1)]=1  #onehot 编码
#em=em.reshape(2,2,3)

t = Pwe*em
#PWE=np.prod(np.where(t==0,1,t),axis=0)
PWE=np.prod(np.max(t,axis=2),axis=1)