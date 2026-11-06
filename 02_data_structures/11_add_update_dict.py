"""
11_add_update_dict.py
=====================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 5. Dictionaries — Example 2: Add and update information

What this does
--------------
Shows the difference between adding a new key-value pair and updating an
existing key's value in a dictionary.

Run it
------
    python 11_add_update_dict.py
"""

# Create a dictionary with three key-value pairs.
student = {
    "name": "Ama",
    "age": 19,
    "score": 85
}

# Add a new key-value pair ("course").
student["course"] = "Computer Engineering"

# Update an existing key's value ("score").
student["score"] = 90

# Print the updated dictionary.
print(student)
