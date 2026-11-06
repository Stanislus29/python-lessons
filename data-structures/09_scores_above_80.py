"""
09_scores_above_80.py
=====================
Regent University College, Accra, Ghana
Lesson: Data Structures — Lists and Dictionaries
Section: 4. More on lists — Optional extension

What this does
--------------
Loops through a list of scores and prints only the scores that are greater
than or equal to 80. This shows how to combine a loop with an if statement
to filter items in a list.

Run it
------
    python 09_scores_above_80.py
"""

# List of student scores.
scores = [75, 82, 68, 90, 85]

# Print only scores greater than or equal to 80.
for score in scores:
    if score >= 80:
        print(score)
