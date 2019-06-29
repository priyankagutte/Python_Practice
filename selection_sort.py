list=[]
n=int(input(" enter the length of list"))
for i in range(n):
    x=int(input(" enter the elements of list "))
    list.append(x)
print("Original list{}".format(list))

for i in range(len(list)-1):
    pos=i
    for  j in range(i, len(list)):
        if list[j]< list[pos]:
           pos=j
    list[pos], list[i]=list[i], list[pos]
print("Sorted list{}".format(list))