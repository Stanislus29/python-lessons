"""
15_take_home_practice.py
========================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: Take-home practice

What this does
--------------
Take-home practice from the end of the lesson:
  1. Creates a list containing the names of three subjects.
  2. Creates a dictionary for one subject with keys "name", "teacher",
     and "room".
  3. Prints the list.
  4. Prints each value in the dictionary.

Run it
------
    python 15_take_home_practice.py
"""

# Create a list containing the names of three subjects.
subjects = ["Mathematics", "Physics", "Computer Science"]

# Print the list.
print(subjects)

# Create a dictionary for one subject.
subject = {
    "name": "Computer Science",
    "teacher": "Dr. Mensah",
    "room": "Lab 3"
}

# Print each value in the dictionary.
print(subject["name"])
print(subject["teacher"])
print(subject["room"])
