# -*- coding: utf-8 -*-
import numpy as np
filename = 'testfile.test'
persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S30','i', 'f']}, align= True )
a = np.array([("Zhang",32,75.5),("Wang",24,65.2)],
    dtype=persontype)
c = a[1]
c["name"] = "Li"
a.tofile(filename)

b = np.fromfile(filename,dtype=persontype)
print(b[1])
print(b[0]['name'])