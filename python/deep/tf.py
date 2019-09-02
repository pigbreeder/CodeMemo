tensorboard --logdir e2c:model_en2cn/,c2e:model_en2cn/ --port 2333  

# 梯度求解
# https://blog.csdn.net/qq_23981335/article/details/80759714

# None
# None 传默认参数只能判断 if param is not None: do_something()   不能 if is None... 强制要用eager模式

tf.print
# https://stackoverflow.com/questions/54211834/how-to-use-tf-print-not-tf-print-in-high-level-estimator-api

# scope使用
# 变量复用，若想重用则 with tf.variable_scope('shit') as v:，with tf.variable_scope(v) 
# get_variable()。去搜索变量名，然后没有就新建，有就直接用。
#１．　｀tf.variable_scope｀和｀tf.get_variable｀必须要搭配使用（全局scope除外），为share提供支持。
#２．　｀tf.Variable｀可以单独使用，也可以搭配｀tf.name_scope｀使用，给变量分类命名，模块化。
# https://www.zhihu.com/question/54513728/answer/181819324
scope = tf.get_variable_scope()#
with tf.variable_scope('a', reuse=tf.AUTO_REUSE):
	with tf.variable_scope('myscope'):
		scope = tf.get_variable_scope()#
		v=tf.get_variable("v",[1],initializer=tf.constant_initializer(1.0))
		print(tf.Variable(1.0, name='var1'))

with tf.variable_scope('b'):
	with tf.variable_scope(scope):
		print(tf.Variable(1.0, name='var2'))





# 重载入之前的参数 get_assignment_map_from_checkpoint
# https://www.twblogs.net/a/5c4af79abd9eee6e7e06b379/zh-cn
# https://daiwk.github.io/posts/nlp-bert-code-annotated-framework.html


# 读取 tensor summary
# https://blog.csdn.net/little_kid_pea/article/details/79199090
# https://stackoverflow.com/questions/42355122/can-i-export-a-tensorflow-summary-to-csv
import sys
import numpy as np
from tensorboard.backend.event_processing import event_accumulator

def tensor_summary_value_to_variable(v):
    fb = np.frombuffer(v.tensor_proto.tensor_content, dtype = np.float32)
    shape = []
    for d in v.tensor_proto.tensor_shape.dim:
        shape.append(d.size)
    fb = fb.reshape(shape)
    var = fb # var = tf.Variable(fb)
    return var
 
file=sys.argv[1]
num_heads = 16
num_layers = 6
theta = 0.65
epoch_choice = -1
ea = event_accumulator.EventAccumulator(file)
ea.Reload()
# ea.Tags()
# ea.Tensors("transformer/parallel_0_6/transformer/body/decoder/layer_5/encdec_attention/multihead_attention/dot_product_attention/tensor")
# transformer/parallel_0_6/transformer/body/decoder/layer_0/self_attention/multihead_attention/dot_product_attention_relative/tensor
 
self_weights = []
ende_weights = []
for i in range(num_layers):
    self_attn = 'transformer/parallel_0_6/transformer/body/decoder/layer_%s/self_attention/multihead_attention/dot_product_attention_relative/tensor' % i
    ende_attn = 'transformer/parallel_0_6/transformer/body/decoder/layer_%s/encdec_attention/multihead_attention/dot_product_attention/tensor' % i
    se = ea.Tensors(self_attn)[-1]
    en = ea.Tensors(ende_attn)[-1]
    self_weights.append(tensor_summary_value_to_variable(se))
    ende_weights.append(tensor_summary_value_to_variable(en))
