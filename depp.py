import numpy as np
"""
data1=np.zeros((2,10), dtype=int, order='C')
data1[1,4]=1
print(data1)

data1=np.arange(10,49,1)
print(data1)

data1=np.zeros((4,4))
print(data1.dtype.name)
"""
data1=np.arange(64).reshape(4,4,4)
print(data1)
data1=data1.transpose(2,0,1)
print('------------------------')
print(data1)