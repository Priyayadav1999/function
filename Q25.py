def positive_num(x):
    i=0
    c_neg=0
    c_pos=0
    while i<len(x):
        if x[i]>0:
            c_pos+=1
        elif x[i]<0:
            c_neg+=1
        i+=1
    print("total positive numbers=",c_pos)
    print("total negative numbers=",c_neg)

list1 = [2, -7, 5, -64, -14]
positive_num(list1)
