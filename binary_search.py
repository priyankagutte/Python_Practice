list=[]
n=int(input(" enter the length of list"))
for i in range(n):
    x=int(input(" enter the elements of list "))
    list.append(x)
list.sort()
print(list)

s=int(input(" enter the no. you want to serach in list"))

l=0
u=len(list)
if s in list:
    for i in range(len(list)):
        m=int((l+u)/2)
        if list[m] == s:
            print("found at {}".format(m+1))
            break
        elif s>list[m]:
            l=m
        else:
            u=m

else:
    print(" not in list ")