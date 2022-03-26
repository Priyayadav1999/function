def prime(limit):
    i=1
    while i<=limit:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c=c+1
            j+=1
        if c==2:
            print("Prime number=",i)
        i+=1
n=int(input("enter limit="))
prime(n)         