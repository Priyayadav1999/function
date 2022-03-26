def multiply(x):
    i=0
    while i<x:
        n=int(input("enter number="))
        if n%2==0:
            print(n*100)
        else:
            print(n*-1)
        i+=1
num=int(input("enter nth term="))
multiply(num)