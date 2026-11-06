"""
08_average_score.py
===================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 4. More on lists — Practical example: Calculate the average score

What this does
--------------
Stores students' scores in a list and calculates the average score using
sum() and len(). Because the calculation uses sum() and len() rather than
fixed values, adding another score to the list automatically updates the
average.

Run it
------
    python 08_average_score.py
"""

# Store the students' scores in one list.
scores = [75, 82, 68, 90, 85]

# Add all the scores together.
total = sum(scores)

# Count how many scores there are.
number_of_students = len(scores)

# Divide the total by the count to get the average.
average = total / number_of_students

# Print the results.
print("Total score:", total)
print("Number of students:", number_of_students)
print("Average score:", average)
