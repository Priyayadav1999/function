def myfun(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0:
            sum+=i
        elif i%5==0:
            sum+=i
        i+=1
    print(sum)

a=int(input("enter your number"))
myfun(a)
