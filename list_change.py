def list_change(x,y):
    a=[]
    i=0
    while i<len(x):
        multiply=1
        multiply=multiply*x[i]*y[i]
        a.append(multiply)
        i+=1
    return a    

multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print(multiple_list)