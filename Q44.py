def my_fun(x):
    n=int(input("enter nth term="))
    i=1
    while i<=n:
        print(x[-i])
        i+=1
list=['a',1,'2',5,'b','q']
my_fun(list)