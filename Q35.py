def my_fun(age):
    if age <14:
        return "Drink Toddy"
    elif age<18:
        return "Drink Coke"
    elif age<21:
        return "Drink Beer"
    elif age>=21:
        return "Drink whiskey"

age1=int(input("enter age="))
print(my_fun(age1))
