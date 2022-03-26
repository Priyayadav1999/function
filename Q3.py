def sum_num(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i+=1
    return sum


list=(8, 2, 3, 0, 7)
print(sum_num(list))