def uppercase_str(n):
    i=0
    while i<len(n):
        if n[i]=="a":
            n[i]="A"
        i+=1
    print(n)




str=input("enter string=")
uppercase_str(str)