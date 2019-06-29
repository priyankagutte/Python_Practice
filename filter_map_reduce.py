from functools import reduce
l1=[]
for i in range(1,100):
    l1.append(i)
print(l1)

""" using filter """
even=list(filter(lambda a:a%2==0 , l1))
print(even)

""" using map"""
cube=list(map(lambda a:a**3,even))
print(cube)

""" using reduce (we need to import functtools module ) """
sum=reduce(lambda a,b:a+b ,cube)
print(sum)