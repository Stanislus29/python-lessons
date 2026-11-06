"""
dog_class.py
============
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - a Dog class

What this does
--------------
Defines a Dog class with a name and age, and a bark() method that returns
the sound the dog makes. A main() block creates two dogs and prints what
each one says.

Students learn:
  * defining a class with attributes (name, age)
  * defining a method (bark) that uses self
  * creating object instances and calling their methods
  * the if __name__ == "__main__" guard

Run it
------
    python dog_class.py
"""


class Dog:
    """Represents a dog with a name and an age.

    Attributes:
        name (str): The dog's name.
        age (int): The dog's age.
    """

    def __init__(self, name, age):
        """Initialise the dog with a name and an age."""
        self.name = name
        self.age = age

    def bark(self):
        """Return the sound the dog makes."""
        return f"{self.name} says Woof!"


def main():
    """Create two dogs and print what each one says."""
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    print(dog1.bark())   # Buddy says Woof!
    print(dog2.bark())   # Max says Woof!


if __name__ == "__main__":
    main()
