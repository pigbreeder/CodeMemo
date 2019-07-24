# -*- coding: utf-8 -*-
#Python拷贝(深拷贝deepcopy与浅拷贝copy)
>>> import copy
>>> a = [1,2,3,4,['a','b']]  #原始对象

>>> b = a  #赋值，传对象的引用

>>> c = copy.copy(a)

>>> d = copy.deepcopy(a)

>>> a.append(5)
>>> a[4].append('c')

>>> print 'a=',a
a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
>>> print 'b=',b
b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
>>> print 'c=',c
c= [1, 2, 3, 4, ['a', 'b', 'c']]
>>> print 'd=',d
d= [1, 2, 3, 4, ['a', 'b']]