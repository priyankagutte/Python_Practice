list=[]
n=int(input(" enter the length of list"))
for i in range(n):
    x=int(input(" enter the elements of list "))
    list.append(x)
print("Original list{}".format(list))
for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            list[j],list[j+1]= list[j+1],list[j]
print("Sorted list{}".format(list))
