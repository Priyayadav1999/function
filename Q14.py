def prime_num(x):
    i=1
    c=0
    while i<=x:
        if x%i==0:
            c+=1
        i+=1
    if c==2:
        print(x,"is a prime number")
    else:
        print(x,"is not a prime number")
    
num=int(input("enter number="))
prime_num(num)
