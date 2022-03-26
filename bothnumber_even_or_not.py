def check_numbers(x,y):
    if x%2==0 and y%2==0:
        print("Dono even hain")
    else:
        print("dono even nhi hain")
a=int(input("enter number="))
b=int(input("enter number="))
check_numbers(a,b)

     # 2ND METHOD       ######
# def check_numbers_list(x,y):
#     i=0
#     while i<len(x):
#         if x[i]%2==0 and y[i]%2==0:
#             print("Dono Even hain")
#         else:
#             print("Dono Even nahi hain")
#         i+=1
# a=[2, 6, 18, 10, 3, 75]
# b=[6, 19, 24, 12, 3, 87] 
# check_numbers_list(a,b)
