def unique_list(a):
    i=0
    new_list=[]
    while i<len(a):
        if a[i] not in new_list:
            new_list.append(a[i])
        i+=1

    return new_list


list=[1,2,3,3,3,3,4,5]
print(unique_list(list))