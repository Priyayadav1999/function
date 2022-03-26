def perfect(a):
    i=1
    while i<a:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum==i:
            print(i,"is a perfect number")
        # else:
        #     print(i,"is not a perfect number")
        i+=1

x=int(input("enter your nth number"))
perfect(x)