""" creating two dimentional arrayu (matrix) """
from numpy import *
"""a = array ([
          [1,2,0,4,5,1],
          [0,6,7,0,2,6]
          ])
print(a)"""
""" operation """

""""print(a.shape,a.size,a.sum(),a.copy(),a.all(1))
print(a.any(),a.argmax(),a.argmin(),a.argsort())"""

""" matix indexing """

"""print(a[0,3])
print(a[1,3])"""

""" converting of array 
b=a.flatten()
print(b)

c=b.reshape(2,2,3)
print(c)

print("-------------")

z=b.reshape(4,3)
print(z)

print("----------------------------")
""" creating matrix """"""

m=matrix(a)
print(m)

"""" user defined matrix """

m1=matrix('1 2 3 ; 2 3 4 ; 4 5 6')
print(m1)
print("------------------------------")


"""" addition and multiplication of matrix """
m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
sum= m1+m2
mul=m1*m2
print( mul)

z=0
r=matrix('')
for i in range(1,4):
    for j in range (1,4):
        z[i,j]=m1[i,j]*m2[ij]
        z=z[i,j]+z
print(z)

