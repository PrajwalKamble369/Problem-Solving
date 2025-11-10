print("""
Modules:
      There are inbuild as well as user built modules in python.
      Module can collection of function,variable, class
\n""")

# creating module 

# creating greeting

def greeting(name):
    return "Hello {name}, Welcome to python learning !"

# list addition
def list_add(a=[]):
    return sum(a)

# list multiplocation
def list_multi(a=[]):
    multi = 1
    for i in a:
        multi = i * multi
    return multi


def calcu():
    print("Enter the operations [+,-,/,*]")
    op = input("Enter operation, [+,-,/,*]")
    if op == "+":
        num1 = eval(input("Enter number1"))
        num2 = eval(input("Enter number 2"))
        return num1+num2
    
    elif op == "-":
        num1 = eval(input("Enter number1"))
        num2 = eval(input("Enter number 2"))
        return num1 - num2

    elif op == "*":
        num1 = eval(input("Enter number1"))
        num2 = eval(input("Enter number 2"))
        return num1 * num2

    elif op == "/":
        num1 = eval(input("Enter number1"))
        num2 = eval(input("Enter number 2"))
        return  num1 / num2
    else:
        return "enter correct operation"
