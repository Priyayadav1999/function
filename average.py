def myfun(z):
    i=0
    sum=0
    while i<z:
        a=int(input("enter number"))
        sum=sum+a
        i+=1
    average=sum/z
    print("Sum of three numbers :-",sum)
    print("Average of three numbers :-",average)
myfun(3)