def count_sheep(n):
    i=0
    c=0
    while i<len(n):
        if n[i]==True:
            c+=1
        i+=1
    print("Total number of sheep=",c)


list=[True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True]
count_sheep(list)