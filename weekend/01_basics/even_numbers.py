"""
even_numbers.py
===============
Regent University College, Accra, Ghana
Python for Beginners - Weekend Session
Topic: Loops and identifying even numbers

What this does
--------------
Loops through a list of numbers and prints a message for each even number,
noting that it is being divided by 2.

Students learn:
  * looping over a list by index with range(len(...))
  * the modulo operator % to test whether a number is even (remainder 0)
  * a while loop combined with break to run an action once per match

Run it
------
    python even_numbers.py
"""

numbers = [10, 12, 15, 22, 25, 30, 35, 40, 45]

# Check each number by its index.
for i in range(len(numbers)):
    # While the current number is even (remainder 0 when divided by 2)...
    while numbers[i] % 2 == 0:
        print(f"{numbers[i]} is even, dividing by 2")
        # ...print once, then stop checking this number.
        break
