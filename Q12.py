def ending_num(a):
    while a>0:
        k=a%10
        if k!=0:
            break
        a=a//10
    return a
n=int(input("enter a number"))
print(ending_num(n))