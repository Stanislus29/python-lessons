"""
conditionals.py
===============
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Loops and conditional (if) statements

What this does
--------------
Loops through a list of numbers, prints each one, and detects whether any
number is greater than 10. When a number greater than 10 is found it prints
a message and stops looking (using break).

Students learn:
  * iterating over a list with for
  * the if statement to test a condition
  * using break to exit a loop early

Run it
------
    python conditionals.py
"""

# A list of numbers to check.
# NOTE: we avoid naming this 'list' because that shadows the built-in list type.
values = [6, 7, 9, 12, 15, 18, 21, 4, 3, 6, 13, 14, 15]

# Flag that becomes True once we find a number greater than 10.
found_large_number = False

for i in values:
    print(i)

    if i > 10:
        print('Condition met:', i)
        found_large_number = True

        # We found what we were looking for, so stop looping.
        if found_large_number:
            print('There is a number greater than 10 in the list')
            break
