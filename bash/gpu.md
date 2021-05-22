# kill gpu
fuser -v /dev/nvidia*

# 多gpu下模型存储
DataParallel包装的模型在保存时，权值参数前面会带有module字符，然而自己在单卡环境下，没有用DataParallel包装的模型权值参数不带module。本质上保存的权值文件是一个有序字典。

使用pytorch的rank看来存储
https://www.cnblogs.com/wildkid1024/p/13025352.html

# 查看GPU使用
watch -n1 nvidia-smi