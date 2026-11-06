"""
adult_or_minor.py
=================
Regent University College, Accra, Ghana
Python for Beginners - Weekend Session
Topic: Conditional (if / else) statements

What this does
--------------
Asks the user for their age and prints whether they are an adult (18 or
older) or a minor (younger than 18).

Students learn:
  * input() and int() to read a number from the user
  * the comparison operator >= (greater than or equal to)
  * if / else to choose between two outcomes

Run it
------
    python adult_or_minor.py
"""

# Read the user's age and convert it to an integer.
age = int(input("Enter your age: "))

# If the age is 18 or above, the person is an adult; otherwise a minor.
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
