"""
13_dict_get_method.py
=====================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 5. Dictionaries — A useful detail: get()

What this does
--------------
Shows that looking up a missing key with square brackets raises a KeyError,
while the get() method returns a default value instead.

Run it
------
    python 13_dict_get_method.py
"""

# Create a dictionary with two key-value pairs.
student = {"name": "Ama", "score": 90}

# "course" is not a key in this dictionary.
# get() returns a default value instead of raising an error.
print(student.get("course", "Not provided"))   # Expected output: Not provided
