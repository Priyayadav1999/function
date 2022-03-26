def fizz_buzz(x):
    if x%3==0 and x%5==0:
        print("fizzbuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)
num=int(input("enter number="))
fizz_buzz(num)
