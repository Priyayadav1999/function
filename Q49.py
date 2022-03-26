def even_odd(x):
    i=0
    while i<x:
        num=int(input("enter number="))
        if num%2==0:
            print("Even")
        else:
            print("Odd")
        i+=1
n=int(input("enter nth term="))
even_odd(n)