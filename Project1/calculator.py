import time
# Define addition function


def add(x, y):
    return (x+y)

# Define subtraction function


def sub(x, y):
    return (x-y)

# Define multiplication function


def mul(x, y):
    return (x*y)

# Define division function


def div(x, y):
    return (x/y)


print("Choose form the following functions: ")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

time.sleep(2)

user_input = int(input("Select operation: 1,2,3,4: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if user_input == 1:
    print(num1 + " + " + num2 + " = " + add(num1, num2))
elif user_input == 2:
    print(num1 + " - " + num2 + " = " + sub(num1, num2))
elif user_input == 3:
    print(num1 + " * " + num2 + " = " + mul(num1, num2))
elif user_input == 4:
    print(num1 + " / " + num2 + " = " + div(num1, num2))
else:
    print("Invalid input. Try again!")
