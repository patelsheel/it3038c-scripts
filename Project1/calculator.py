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


def main():

    while True:
        print("Hello, welcome to the calculator app!")

        time.sleep(1)

        print("The app will calculate all 4 operations itself \n i.e. addition, subtraction, multiplication, division. ")

        time.sleep(1)

        print("Ready or not here we go...")

        time.sleep(1)

        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter  your second number: "))

        print(num1, "+", num2, "=", add(num1, num2))
        print(num1, "-", num2, "=", sub(num1, num2))
        print(num1, "*", num2, "=", mul(num1, num2))
        print(num1, "/", num2, "=", div(num1, num2))
        calculate_again = input("Do you want to again? [yes/no]")
        if calculate_again == "no" or "N" or "No" or "n":
            exit("GoodBye!")


main()
