"""
02_create_access_list.py
========================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 2. Lists — Example 1: Create and access a list

What this does
--------------
Creates a list of student names and shows how to:
  * print the whole list
  * access individual items by index (Python counts from 0)
  * count the number of items with len()

Students learn that the first item is at index 0, not index 1.

Run it
------
    python 02_create_access_list.py
"""

# Create a list of student names.
students = ["Ama", "Kojo", "Esi", "Yaw"]

# Print the whole list.
print(students)

# Access individual items by index. Index 0 is the first item.
print(students[0])   # First item -> "Ama"
print(students[2])   # Third item -> "Esi"

# Count how many items are in the list.
print(len(students))  # Number of items
