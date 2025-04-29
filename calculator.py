import math

a = float(input("Type in the first number:"))
b = float(input("Type in the second number:"))

print(" Select: \n1. Add \n2. Subtract \n3. Divide \n4. Multiply \n5. Square root")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def square_root(a):
    return math.sqrt(a)


equation = input()

# Equation
if equation.lower() == "add" or equation == "1":
    print("Result:", add(a, b))
elif equation.lower() == "subtract" or equation == "2":
    print("Result:", subtract(a, b))
elif equation.lower() == "divide" or equation == "3":
    print("Result:", divide(a, b))
elif equation.lower() == "multiply" or equation == "4":
    print("Result:", multiply(a, b))
elif equation.lower() == "sqrt" or equation == "5":  # Only uses the first number for square root
    print("Result:", square_root(a))
else:
    print("Invalid selection.")
