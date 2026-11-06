"""
07_list_operations.py
=====================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 4. More on lists — Useful list operations

What this does
--------------
Demonstrates common list operations:
  * append()  — add an item to the end
  * remove()  — remove the first matching item
  * sort()    — sort the list in place
  * len()     — count the number of items
  * sum()     — add numeric items together

Run it
------
    python 07_list_operations.py
"""

# Start with a list of numbers.
numbers = [7, 2, 9, 4]

# Add 6 to the end.
numbers.append(6)

# Remove the first matching 2.
numbers.remove(2)

# Sort the list in ascending order.
numbers.sort()

# Print the modified list.
print(numbers)

# Print the number of items.
print(len(numbers))     # Number of items

# Print the sum of the numeric items.
print(sum(numbers))     # Sum of numeric items
