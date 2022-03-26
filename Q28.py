def show_numbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print("Even=",i)
        else:
            print("Odd=",i)
        i+=1
a=int(input("enter limit="))
show_numbers(a)