from http.client import PRECONDITION_REQUIRED
import numpy as np
from regex import B
"""
data1=np.zeros((2,10), dtype=int, order='C')
data1[1,4]=1
print(data1)

data1=np.arange(10,49,1)
print(data1)

data1=np.zeros((4,4))
print(data1.dtype.name)

A=[ [1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]]
print(A)
print(A[0])
print(A[1][1])
print(A[0][-1])
column=[]
for row in A:
    column.append(row[2])
print(column)

A=[ [1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]]

B=[ [1,4,5,12],
    [-5,8,9,0],
    [-6,7,11,19]]

C=[ [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j]=A[i][j]+B[i][j]
for r in C:
    print(r)

A=[ [1,4],
    [-5,8],
    [-6,7]]

C=[ [0,0,0],
    [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        C[j][i]=A[i][j]
for r in C:
    print(r)


a = np.array([1,2,3])
print(a)
print(type(a))

A= np.array([[1,2,3],[3,4,5]])
print(A)
A= np.array([[1.1,2,3],[3,4,5]])
print(A)
A= np.array([[1,2,3],[3,4,5]], dtype=complex)
print(A)


zeros_array=np.zeros((2,3))
print(zeros_array)
ones_array=np.ones((1,5), dtype=np.int64)
ones_array[0][0]=8589934592
print(ones_array)

A=np.arange(4)
print(A)
B=np.arange(12).reshape(2,6)
print(B)

A=np.array([[2,4,6],[5,6,7]])
B=np.array([[9,-3],[3,-6],[4,6]])
#C=A+B
C=A.dot(B)
D=np.array([0,1,2,3,4,5,6,7,8,9])
print(C)
print(A)
print(A.transpose())
print(A[1])
print(A[:,2])
print(D[2:5])

"""
a=np.arange(10,50,1)
#print(a)
#a_inv=a[::-1]
b=np.arange(9).reshape(3,3)
k=np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
d=np.identity(6)
#np.argwhere( k!=0 )
e=np.random.rand(3,3,3)
print(e.argmax())
print(e.ravel()[e.argmax()])
print(e)
print(np.unravel_index(e.argmax(), e.shape))
print(e[np.unravel_index(e.argmax(), e.shape)])
