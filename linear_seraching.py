# in linear search we have to search the specified value one by one (using for or while loop) and provide its position


l=[]
n=int(input(" enter the length of list"))
for i in range(n):
    x=int(input(" enter the elements of list "))
    l.append(x)
print(l)
search=int(input(" enter the no. you want to serach in list"))
if search in l:
    for i in range(n):
        if l[i]==search:
            print(" found at position {}".format(i+1))
else:
    print("not in list")