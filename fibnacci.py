
n=int(input(" enter no. of elements in your fibnacci series "))
def fibnacci(n):
    a=0
    b=1
    if n<=0:
        print(" enter a valid number which is greater than 0 ")
    elif n==1:
        print(a)
    else:
        print(a,b , end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c, end= " ")


fibnacci(n)

""" if we want series tiil user specified number """

n=int(input(" enter no. of elements in your fibnacci series "))
def fibnacci(n):
    a=0
    b=1
    if n<=0:
        print(" enter a valid number which is greater than 0 ")
    elif n==1:
        print(a)
    else:
        print(a,b , end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if n>=c:
                print(c, end= " ")


fibnacci(n)

