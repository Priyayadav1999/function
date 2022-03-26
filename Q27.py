def speed_drivers(speed):
    
    if speed<=70:
        print("OK")
    if speed>70:
        points=(speed-70)//5
        if points<=12:
            print("Points=",points)
        else:
            print("License Suspended")
total_speed=int(input("enter speed of driver"))
speed_drivers(total_speed)