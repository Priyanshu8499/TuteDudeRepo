# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
inp = int(input("Enter a Number: "))

if inp % 2 == 0:
    print(f"{inp} is an Even Number")
else:
    print(f"{inp} is an Odd Number")
