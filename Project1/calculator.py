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


user_input = int(input("Select operation: 1,2,3,4: "))
time.sleep(2)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if user_input == 1:
    print(add(num1, num2))
elif user_input == 2:
    print(sub(num1, num2))
elif user_input == 3:
    print(mul(num1, num2))
elif user_input == 4:
    print(div(num1, num2))
else:
    print("Invalid input. Try again!")


def again():
    return


# again_input = input("Calculate again? : Y or N \n")
# if again_input == "y" or "Y":
#     calculator()
# else:
#     exit()
