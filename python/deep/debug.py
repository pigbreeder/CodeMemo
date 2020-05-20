
# 查看变量增长位置
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