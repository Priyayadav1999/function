def multiplication_table(n):
    i=1
    while i<=10:
        print(n,"*",i,"=",n*i)
        i+=1
num=int(input("enter number="))
multiplication_table(num)