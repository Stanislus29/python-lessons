"""
10_create_access_dict.py
========================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 5. Dictionaries — Example 1: Create and access a dictionary

What this does
--------------
Creates a dictionary storing one student's details as key-value pairs and
shows how to look up values by key ("name" and "score").

Run it
------
    python 10_create_access_dict.py
"""

# Create a dictionary with key-value pairs.
student = {
    "name": "Ama",
    "age": 19,
    "score": 85
}

# Look up values using their keys.
print(student["name"])   # "Ama"
print(student["score"])  # 85
