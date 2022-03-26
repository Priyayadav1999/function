def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def divi(x,y):
    print(x/y)

def modul(x,y):
    print(x**y)

def calculator():
    while True:
        a = input("enter number =")
        b = input("enter number =")
        c = input("enter symbol(+,-,/,*,**)=")   
        if c == "+":
            add(int(a),int(b))
        elif c == "-":
            sub(int(a),int(b))
        elif c == "*":
            mul(int(a),int(b))
        elif c == "/":
            divi(int(a),int(b))
        elif c == "**":
            modul(int(a),int(b))
        elif a or b or c == "n":
            break
calculator()