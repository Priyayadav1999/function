def show_numbers(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"Odd")
        i+=1

a=int(input("enter nth number"))
show_numbers(a)