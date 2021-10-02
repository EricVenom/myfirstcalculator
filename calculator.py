calculator = "On"

def sum():
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    result = x + y
    print(f"The sum of {x} and {y} is: {result}")
    print()

def sub():
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    result = x - y
    print(f"The subtraction of {x} and {y} is: {result}")
    print()

def multi():
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    result = x * y
    print(f"The multiplication of {x} and {y} is: {result}")
    print()

def divide():
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    result = x / y
    print(f"The division of {x} and {y} is: {result}")
    print()

while calculator == "On":
    print("Welcome to calculator 1.0! Choose an operator to proceed. ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    proceed = input("1/2/3/4/5: ")
    if proceed == "1":
        sum()
    elif proceed == "2":
        sub()
    elif proceed == "3":
        multi()
    elif proceed == "4":
        divide()
    elif proceed == "5":
        print()
        print("Goodbye!")
        exit()
    else:
        print()
        print("That's not a valid input. Try again!")
        print()
