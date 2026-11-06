"""
component_and_resistor.py
=========================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - inheritance and encapsulation

What this does
--------------
Defines a base class Component and a subclass Resistor. Resistor inherits
name and type from Component and adds a resistance value (stored as a
"protected" attribute _resistance). It demonstrates:

  * inheritance: class Resistor(Component)
  * super() to call the parent constructor
  * method overriding with super().describe()
  * a simple encapsulation convention: attributes prefixed with _ are
    intended to be treated as internal (read-only-ish)

Students learn:
  * inheritance and code reuse
  * overriding describe() while reusing the parent's version via super()
  * the underscore naming convention for internal attributes

Run it
------
    python component_and_resistor.py
"""


class Component:
    """A generic circuit component with a name and a type.

    Attributes:
        name (str): The component's name (e.g., "R1").
        type (str): The component's type (e.g., "resistor").
    """

    def __init__(self, name, type):
        """Initialise the component with a name and a type."""
        self.name = name
        self.type = type

    def describe(self):
        """Return a short description of the component."""
        return f"{self.name}: {self.type}"


class Resistor(Component):
    """A resistor: a Component that also has a resistance in ohms.

    Attributes:
        name (str): inherited from Component
        type (str): inherited from Component
        _resistance (float): resistance in ohms (internal by convention)
    """

    def __init__(self, name, type, resistance):
        """Initialise the resistor with name, type, and resistance."""
        super().__init__(name, type)
        self._resistance = resistance

    def describe(self):
        """Return a description including the resistance value."""
        base = super().describe()   # reuse the parent's description
        return f"{base}, {self._resistance} ohms"


def main():
    """Create a resistor, change its resistance, and describe it."""
    r = Resistor("R1", "resistor", 220)

    # _resistance is "protected" by convention: code outside the class
    # *can* change it, but it signals "treat this as internal."
    r._resistance = 330   # update the resistance value

    print(r.describe())   # R1: resistor, 330 ohms


if __name__ == "__main__":
    main()
