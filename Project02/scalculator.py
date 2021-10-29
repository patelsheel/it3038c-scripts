import math
import time


def add(x, y):
    return(x+y)


def sub(x, y):
    return(x-y)


def Main():
    print("Hello, again!")
    time.sleep(1)
    print("Welcome Back! We have made some changes since you were gone.")
    time.sleep(1)
    print("You can now choose the operation you want to do. And we have added support for scientific calculations.")
    print("After you choose the operation based on the operation, you'll be presented to input the numbers of your choice.")
    time.sleep(2)
    print(""" 
        press -  
        1 - Addition
        2 - Subtraction
        3 - Multiplication
        4 - Division
        5 - Exponents
        6 - Tan
        7 - Sin
        8 - Cos
        9 - Factorial
        10 - Log(x) 
        """)

    i = input("Enter your operation: ")

    if i == "1":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(x + y)

    elif i == "2":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(x-y)

    elif i == "3":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(x*y)

    elif i == "4":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(x/y)

    elif i == "5":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(x**y)

    elif i == "6":
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))
        print(math.tan(x))

    elif i == "7":
        x = int(input("Enter your number: "))
        print(math.sin(x))

    elif i == "8":
        x = int(input("Enter your number: "))
        print(math.cos(x))

    elif i == "9":
        x = int(input("Enter your number: "))
        print(math.factorial(x))

    elif i == "10":
        x = int(input("Enter your number: "))
        print(math.log(x))

Main()
