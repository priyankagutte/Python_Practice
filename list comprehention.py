""" alloes to creat new list based on exciting list with some condition """
""" it always returns list only """

a=[1,2,3,4,5,6,7,8,9]
print(a)
a1=[n*n for n in a]
print(a1)
a2=[n*n for n in a if n%2==0]
print(a2)

""" coping list without build-in method """
b=[i for i in a]
print(b)

print("-----------------")

k=[]
n=int(input(" enter length of list"))
for i in range(n):
    x=int(input(" enter values in list "))
    k.append(x)
print(k)
k1=[i for i in k if i%3==0]
print(k1)

print("----------------------------")

