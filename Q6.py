def even_num(a):
    i=0
    new_list=[]
    while i<len(a):
        if a[i]%2==0:
            new_list.append(a[i])
        i+=1
    return new_list

list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_num(list))