""" creating empty text file and writing """
#f=open('text3.txt','w')
#f.write("sjhbjhdbvjshb hsjkfbskfj ")

""" reading the file """
#f=open('text3.txt','r')
#print(f.read())

"""" opening the image file """
f1=open('j1.JPG','wb')
f=open('j.JPG','rb')
print(f.read())
for i in f:
    f1.write(i)


