def maximum(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    return max

n=[4,6,2,1,9,63,-134,566]
print(maximum(n))


def minimum(b):
    i=0
    min=b[i]
    while i<len(b):
        if b[i]<min:
            min=b[i]
        i+=1
    return min
num=[-52, 56, 30, 29, -54, 0, -110]
print(minimum(num))