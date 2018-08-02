#!/usr/bin/python
#coding=utf8
# https://blog.csdn.net/chenyulancn/article/details/8203763
# dict 是obj和其他数据格式的桥梁
# 接收参数使用**kwargs, 然后json读取默认配置为dict, 再更新接收的参数
# https://github.com/chenyuntc/PyTorchText/blob/master/main.py
# https://blog.csdn.net/u010099080/article/details/70332074 Fire
import json
from collections import namedtuple

print('obj2dict>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# obj2dict
class Foo(object):
    bar = 'hello'
    baz = 'world'
    def __init__(self):
        self.a = 'AA'

f = Foo()
#1
print(dir(f),vars(f)) # 仅能转换self的属性
print([name for name in dir(f) if not name.startswith('__')])
#2
dict((name, getattr(f, name)) for name in dir(f) if not name.startswith('__'))
#3
def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr
d = props(f)
print(d)
print('更新obj')
kwargs = {'a':'AaA'}
# if opt.debug:import ipdb;ipdb.set_trace()
for k,v in kwargs.iteritems():
    if not hasattr(f,k):
        raise Exception("opt has not attribute <%s>" %k)
    setattr(f,k,v) 
print(props(f))
print('dict2object>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#dict2object
d_named = namedtuple('Struct', d.keys())(*d.values())
print('d_named=', d_named)
print('json2dict>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#json2dict
data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
x = json2obj(data)
print('json2dict=', x)

print('obj动态绑定属性')
f.haha = 'haha'
print(f.haha)
