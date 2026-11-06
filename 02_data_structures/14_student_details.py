"""
14_student_details.py
=====================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 6. Student mini-exercise: dictionaries — Store a student's details

What this does
--------------
Complete solution to the mini-exercise. It:
  1. Creates a dictionary named student with name "Kojo", age 20, score 78.
  2. Prints the student's name.
  3. Updates the score to 88.
  4. Prints the updated dictionary.

Run it
------
    python 14_student_details.py
"""

# Create a dictionary with the three required key-value pairs.
student = {
    "name": "Kojo",
    "age": 20,
    "score": 78
}

# Print the student's name.
print(student["name"])

# Update the score to 88.
student["score"] = 88

# Print the updated dictionary.
print(student)
