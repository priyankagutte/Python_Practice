n=int(input(" enter no. for factorial "))
def factorial(n):
    cout = 1
    for i in range (1,n+1):
        cout=cout*i
    print(cout)
factorial(n)