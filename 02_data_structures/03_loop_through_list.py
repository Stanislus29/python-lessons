"""
03_loop_through_list.py
=======================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 2. Lists — Example 2: Loop through a list

What this does
--------------
Creates a list of student names and uses a for loop to visit each item and
print it. The loop variable student takes the value of the current item on
each iteration.

Run it
------
    python 03_loop_through_list.py
"""

# Create a list of student names.
students = ["Ama", "Kojo", "Esi", "Yaw"]

# Visit each item in the list and print it.
for student in students:
    print(student)
