def count_numbers(a):
    i=0
    count=0
    a[i].split()
    while i<len(a):
        j=0
        k=a[i][j]
        print(a[i][j])
        while j<len(a[i]):
            j+=1
        if k==a[i][j-1]:
            count+=1
        i+=1
    print(count)


list=['abc', 'xyz', 'aba', '1221']
count_numbers(list)
