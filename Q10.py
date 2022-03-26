def sum_num(x,y):
    if x ==" " and y ==" ":
        x=0
        y=0
        return x+y
    elif x==" ":
        x=0
        return x+int(y)
    elif y==" ":
        y=0
        return int(x)+y
    else:
        return int(x)+int(y)
a=input("enter number=")
b=input("enter number=")
print(sum_num(a,b))