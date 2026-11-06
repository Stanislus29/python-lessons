"""
polymorphism.py
===============
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - polymorphism

What this does
--------------
Defines a base class Component with two subclasses: Resistor and Capacitor.
Each subclass overrides describe() to report its own details. A single loop
then calls describe() on every object in a mixed list, without needing to
check each object's type.

This is polymorphism: the same method name (describe) behaves differently
depending on the actual class of each object.

Students learn:
  * inheritance from a common base class
  * overriding methods in subclasses
  * polymorphism: treating different objects uniformly through a shared
    method name
  * iterating over a heterogeneous list

Run it
------
    python polymorphism.py
"""


class Component:
    """A generic circuit component.

    Attributes:
        name (str): The component's name.
        type (str): The component's type.
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        return f"{self.name}: {self.type}"


class Resistor(Component):
    """A resistor: a Component with a resistance in ohms."""

    def __init__(self, name, type, resistance):
        super().__init__(name, type)
        self.resistance = resistance

    def describe(self):
        base = super().describe()
        return f"{base}, {self.resistance} ohms"


class Capacitor(Component):
    """A capacitor: a Component with a capacitance (farads) and a usage."""

    def __init__(self, name, type, capacitance, usage):
        super().__init__(name, type)
        self.capacitance = capacitance
        self.usage = usage

    def describe(self):
        base = super().describe()
        return f"{base}, {self.capacitance} farads, {self.usage}"


def main():
    """Create a mixed list of components and describe each one."""
    components = [
        Resistor("R1", "resistor", 220),
        Capacitor("C1", "capacitor", 1000, "filter"),
    ]

    # The loop does not care whether each item is a Resistor or Capacitor.
    # It calls describe() and each object answers in its own way.
    for c in components:
        print(c.describe())


if __name__ == "__main__":
    main()
