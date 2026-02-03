# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Addition: {a + b}")
print(f"Substraction:{a - b}")
print(f"Multiplication: {a * b}")

if b != 0:
    print(f"Division: {a / b}")
else:
    print("Division: cannot divide by zero")