
###################################    RIGHT HAINNNNN
#  def calculator(x,y,z):
#     if z=="+":
#         add_result=x+y
#         number_1=add_result
#     elif z=="-":
#         subtract_result=x-y
#         number_2=subtract_result 
#     elif z=="*":
#         multiply_result=x*y
#         number_3=multiply_result 
#     elif z=="/":
#         divide_result=x/y
#         number_4=divide_result
# a=int(input("enter your number="))
# b=int(input("enter your number="))
# c=input("enter yopur operation(+,-,*,/)=")
# calculator(a,b,c)


def calculator(a,b,c,d):
    
    print(a,b,c,d)
def add_result(x,y):
    sum=x+y
    return sum
def subtract_result(x,y):
    sub=x-y
    return sub 
def multiply_result(x,y):
    multi=x*y
    return multi 
def divide_result(x,y):
    divide=x/y 
    return divide 
x1=int(input("enter your number="))
y1=int(input("enter your number="))

p=add_result(x1,y1)
q=subtract_result(x1,y1)
r=multiply_result(x1,y1)
s=divide_result(x1,y1)
calculator(p,q,r,s)
