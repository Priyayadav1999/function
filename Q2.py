def three_max(a):
    i=0
    max=0
    while i<len(a):
        if max<a[i]:
            max=a[i]
        i+=1
    j=0
    second_max=0
    while j<len(a):
        if a[j]!=max:
            if second_max<a[j]:
                second_max=a[j]
        j+=1
    k=0
    third_max=0
    while k<len(a):
        if a[k]!=max and a[k]!=second_max:
            if third_max<a[k]:
                third_max=a[k]
        k+=1
    print("first max number=",max)
    print("second max number=",second_max)
    print("third max number=",third_max)
list=[12,4,56,6,3,5,45,67,8,54]
three_max(list)