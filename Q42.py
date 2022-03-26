def list_sum(a):
    i=0
    k=[]
    while i<len(a):
        b=a[i]
        sum=0
        while b>0:
            sum=sum+b%10
            b=b//10
        k.append(sum)
        i+=1
    return k
list=[15, 81, 11, 234]
print(list_sum(list))