"""
06_shopping_list.py
===================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 3. Student exercise: lists — Manage a shopping list

What this does
--------------
Complete solution to the shopping list exercise. It:
  1. Creates a list with "Rice", "Eggs", and "Tomatoes".
  2. Prints the original list.
  3. Adds "Milk" to the list.
  4. Prints the updated list.
  5. Prints the second item in the list.

Expected output:
    ['Rice', 'Eggs', 'Tomatoes']
    ['Rice', 'Eggs', 'Tomatoes', 'Milk']
    Eggs

Run it
------
    python 06_shopping_list.py
"""

# 1. Create a list containing three items.
shopping_list = ["Rice", "Eggs", "Tomatoes"]

# 2. Print the original list.
print(shopping_list)

# 3. Add "Milk" to the list.
shopping_list.append("Milk")

# 4. Print the updated list.
print(shopping_list)

# 5. Print the second item in the list (index 1).
print(shopping_list[1])
