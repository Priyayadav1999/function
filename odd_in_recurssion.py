def sum(a):
    if a==0:
        if a%2!=0:
            print(a)
    else:
        k=sum(a-1)
        if a%2!=0:
            print(a)
sum(10)