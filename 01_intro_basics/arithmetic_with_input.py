"""
arithmetic_with_input.py
========================
Regent University College, Accra, Ghana
Python for Beginners - Weekend Session
Topic: Reading user input and basic arithmetic

What this does
--------------
Asks the user to enter two numbers, reads them as integers, and prints their
sum, product, and quotient. It also checks whether the first number is a
factor of the second (i.e. divides it evenly) and prints the result.

Students learn:
  * input() to read text from the keyboard
  * int() to convert input text into whole numbers
  * arithmetic operators: +, *, /
  * the modulo operator % to test divisibility
  * if / else to branch based on a condition

Run it
------
    python arithmetic_with_input.py
"""

# Read two numbers from the user and convert them to integers.
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

# Print the sum, product, and quotient.
print(x + y)
print(x * y)
print(x / y)

# Check whether x is a factor of y (y divides evenly by x).
if x % y == 0:
    print("Is factor")
else:
    print("Is not a factor")
