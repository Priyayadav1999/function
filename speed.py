def myfun(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        points=(speed-70)//5
        if points<=12:
            print(points)
        else:
            print("license suspended")

x=int(input("enter speed"))
myfun(x)