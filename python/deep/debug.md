
## situation
\x1c 错误可能是CUDA内存被占用
## 查看变量增长位置
```
# before_fairseq_model >>>>>>>>>>>>>>>>>>>>
# 7305937 57672 <<<<<<<<<<<<<<<<<<<<
# 7305937 112848 transformer_encoder_forward <<<<<<<<<<<<<<<<<<<<
# 7305937 111176 encoder_out <<<<<<<<<<<<<<<<<<<<
# 7305937 364104 transformer_decoder_extract_feature <<<<<<<<<<<<<<<<<<<<
# 7305937 74424584 output_layer <<<<<<<<<<<<<<<<<<<<
# 7305937 364104 decoder_out <<<<<<<<<<<<<<<<<<<<
# 7305937 74426256 transformer_encoder_forward <<<<<<<<<<<<<<<<<<<<
# xbost_pre_edit 7305937 74572784 <<<<<<<<<<<<<<<<<<<<
# xbost_post_edit 7305937 148759816 <<<<<<<<<<<<<<<<<<<<
# after_edit 7305937 222830028 <<<<<<<<<<<<<<<<<<<<
# 
# 第二个 transformer_encoder_forward 是对 edit sample 的encode
# 因为有3个output_layer(original, x_pre, x_post)导致中间参数暴涨3倍(70444565->222830028),train_param 涨50%(4893761->7305937)
# 
# 增加最猛的地方就是output_layer这个位置
# 让他一次性计算，然后拼接起来。
# decoder_states_pre_xbost 这个为什么是post部分的
# 为什么要detach？ori_output 是做为正确性的对比点
import gc
param=0
no_param=0
for obj in gc.get_objects():
    try:
        if torch.is_tensor(obj) or (hasattr(obj,'data') and torch.is_tensor(obj.data)):
            #print(type(obj),obj.size())
            if isinstance(obj, torch.nn.parameter.Parameter):
                param += obj.numel()
            else:
                no_param += obj.numel()
    except:pass
print('edit',param,no_param,'<'*20)
```

- 调试模型，直接把valid的数据复制成train得到debug版本数据
- 先确定维度，每个地方都要清楚
- python -u 不用缓存 避免不能立马看结果
- 有些model参数想要更改
- --model-overrides {'factorized_embed':False,'factorized_embed_dim':128} # key中的''一定要加
- 更换优化器 --reset-optimizer

## 节省内存
	- backward 反向传播多个图 （一个结束就释放避免多个loss）
	- 利用backward的累加性可以减少batch updates-freq参数
	- fp16
	- 大致能提升点内存使用
	- --empty-cache-freq 64

## Nan和inf

```
pytorch 中nan处理
log(0) 和x/0 这种情况得到inf然后nan
https://blog.csdn.net/weixin_41278720/article/details/80778640
https://blog.csdn.net/ONE_SIX_MIX/article/details/90322472
https://blog.csdn.net/github_36923418/article/details/103010097
https://zhuanlan.zhihu.com/p/79046709 # 单纯用mask干掉一部分是不行的，因为是后计算得到nan ，nan*0也是nan。只改变需要改变的。这个例子中mask没用是因为最后的结果是要用到所有的内容
```