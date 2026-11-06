"""
using_dog_class.py
==================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - using and extending a class

What this does
--------------
Imports the Dog class defined in dog_class.py and uses it to create dog
objects. It also defines a GuideDog subclass that inherits from Dog and
adds a new behaviour (guide). This shows both:

  * importing and reusing a class from another file in the same folder
  * inheritance: a child class (GuideDog) reusing and extending a parent
    class (Dog)

Students learn:
  * importing a class from a sibling module: from dog_class import Dog
  * creating objects from an imported class
  * inheritance with class Child(Parent)
  * overriding and adding methods in a subclass

Run it from the 03_oop folder
-----------------------------
    python using_dog_class.py

The import statement works because dog_class.py is in the same folder.
"""

from dog_class import Dog


class GuideDog(Dog):
    """A guide dog: a Dog that can also guide its handler."""

    def guide(self):
        """Return a message describing the guide behaviour."""
        return f"{self.name} is guiding their handler."


def main():
    """Create dogs, including a GuideDog, and demonstrate behaviours."""
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    print(dog1.bark())   # Buddy says Woof!
    print(dog2.bark())   # Max says Woof!

    # A GuideDog IS-A Dog: it inherits bark() and adds guide().
    guide = GuideDog("Rex", 4)
    print(guide.bark())   # Rex says Woof! (inherited from Dog)
    print(guide.guide())  # Rex is guiding their handler.


if __name__ == "__main__":
    main()
