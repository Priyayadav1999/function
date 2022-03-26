def square(a):
    i=0
    a=str(a)
    a.split()
    sum=" "
    while i<len(a):
        k=int(a[i])*int(a[i])
        sum=sum+str(k)
        i+=1
    return sum
num=int(input("enter number="))
print(square(num))