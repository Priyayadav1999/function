def my_fun(x):
    n=int(input("enter nth term="))
    while n>0:
        print(x[-n])
        n=n-1
list=['a',1,'2',5,'b','q']
my_fun(list)