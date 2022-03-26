def fun():
    def num(a):
        global count
        count =0
        i=1
        while i<=a:
            if a%i==0:
                count+=1
            i+=1
    num(int(input("enter a value = ")))
    return count
# print(fun())

def check():
    b=fun()
    if b==2:
        print("yes")
    else:
        print("no")
check()