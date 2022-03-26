def square_num(a):
    k=int(input("enter ending number="))
    i=1
    main_list=[]
    x=[]
    y=[]
    while i<=k:
        x.append(i*i)
        y.append(a*a)
        i+=1
        a-=1
    main_list.append(x)
    main_list.append(y)
    return main_list

n=int(input("enter the nth term"))

print(square_num(n))