"""
working_with_lists.py
=====================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Python lists and common list methods

What this does
--------------
Creates a list of numbers and demonstrates several built-in list methods:
  * append()   - add an item to the end
  * insert()   - add an item at a specific position
  * pop()      - remove an item at a position

Students learn how to create, modify, and inspect a list.

Run it
------
    python working_with_lists.py
"""

# Create a list of numbers.
# NOTE: we do not name the variable 'list', because 'list' is a built-in
# Python type and shadowing it would break other code.
numbers = [1, 2, 3, 4, 5]

print('Original list:', numbers)

# Add the number 2 to the end of the list.
numbers.append(2)
print('After append(2):', numbers)

# Insert the number 0 at the beginning (index 0).
numbers.insert(0, 0)
print('After insert(0, 0):', numbers)

# Remove the first item (index 0) from the list.
numbers.pop(0)
print('After pop(0):', numbers)
