def multiple(limit):
    i=1
    sum=0
    while i<=limit:
        if i*3<=limit:
            print(i*3)
            sum=sum+i*3
        if i*5<=limit:
            print(i*5)
            sum=sum+i*5
        # else:
        #     break
        i+=1
    return sum

n=int(input("enter the limit="))
print(multiple(n))
