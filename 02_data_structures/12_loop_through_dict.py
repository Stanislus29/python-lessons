"""
12_loop_through_dict.py
=======================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 5. Dictionaries — Example 3: Loop through a dictionary

What this does
--------------
Creates a dictionary and loops through it using .items() so that each
iteration gives both the key and its corresponding value.

Run it
------
    python 12_loop_through_dict.py
"""

# Create a dictionary with student details.
student = {
    "name": "Ama",
    "age": 19,
    "score": 90
}

# Loop through the dictionary, accessing each key and its value.
for key, value in student.items():
    print(key, ":", value)
