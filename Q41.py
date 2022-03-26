def min_max_len(a):
    i=0
    max=0
    min=a[i]
    while i<len(a):
        if len(a[i])>len(max):
            max=a[i]
        if len(a[i])<len(min):
            min=a[i]
        i+=1
    print("maximum list length=",len(max))
    print("minimum list length=",len(min))
list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
min_max_len(list)