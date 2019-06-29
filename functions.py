"""def add(y,z):
    x=y+z
    print(x)
add(5,4)



l=[10,11,12,13,14,15,16,17]
def even_odd(l):
    e=0
    o=0
    for i in l:
        if i%2==0:
            e=e+1
        else:
            o=o+1
    print(e,o)
even_odd(l)"""

m=[]
n=int(input(" enter no. of list "))
for i in range(n):
   x=input(" input name ")
   m.append(x)
print(m)
def counting(m):
    cout=0
    for i in m:
        if len(i)>=5:
           cout=cout+1
    print(cout)
counting(m)



