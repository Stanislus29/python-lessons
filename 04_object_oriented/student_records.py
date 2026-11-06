"""
student_records.py
==================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - a first class

What this does
--------------
Defines a Student class that stores a student's name, age, and grade, and
provides an add_points() method to increase the grade. It then creates two
student objects (Ama and Kofi), adds points to each, and prints their
details.

Students learn:
  * defining a class with class Student
  * the __init__ constructor and self
  * storing data as object attributes
  * defining and calling methods on objects
  * creating multiple instances of the same class

Run it
------
    python student_records.py
"""


class Student:
    """Represents a student with a name, age, and grade.

    Attributes:
        name (str): The student's name.
        age (int): The student's age.
        grade (int): The student's current grade.
    """

    def __init__(self, name, age, grade):
        """Initialise a student with a name, age, and starting grade."""
        self.name = name
        self.age = age
        self.grade = grade

    def add_points(self, points):
        """Add points to the student's grade."""
        self.grade += points


def main():
    """Create two students, award points, and print their records."""
    ama = Student("Ama", 20, 85)
    kofi = Student("Kofi", 22, 90)

    ama.add_points(10)   # Ama's grade is now 95
    kofi.add_points(5)   # Kofi's grade is now 95

    print(ama.name, ama.age, ama.grade)   # Ama 20 95
    print(kofi.name, kofi.age, kofi.grade)  # Kofi 22 95


if __name__ == "__main__":
    main()
