from numpy import *
m1 = matrix('1 2 3 ; 4 5 6 ; 1 2 3')
m2 = matrix('1 2 3 ; 4 5 6 ; 1 2 3')

for i in range(3):

    for j in range(3):
        sum = 0
        for k in range(3):
            z = (m1[i, k]*m2[k, j])
            sum = z+sum
        print(sum, end="  ")
    print()
