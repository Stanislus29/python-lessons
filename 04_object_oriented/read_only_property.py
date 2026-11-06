"""
read_only_property.py
=====================
Regent University College, Accra, Ghana
Python for Beginners - Topic: Encapsulation with @property

What this does
--------------
Defines a Resistor class with a name and a resistance. The resistance is
stored internally as _resistance and exposed through a read-only @property.
Outside code can read r.resistance but cannot assign to it without
explicitly reaching for the internal _resistance attribute.

This demonstrates the first step of encapsulation: controlling how an
attribute is accessed from outside the class.

Students learn:
  * the @property decorator to expose an attribute for reading
  * the underscore convention (_resistance) for internal attributes
  * that a property without a setter is read-only

Run it
------
    python read_only_property.py
"""


class Resistor:
    """A resistor with a name and a read-only resistance value.

    Attributes:
        name (str): The resistor's name.
        _resistance (float): Internal resistance in ohms.
    """

    def __init__(self, name, resistance):
        """Initialise the resistor with a name and a resistance."""
        self.name = name
        self._resistance = resistance

    @property
    def resistance(self):
        """Return the resistance value (read-only property)."""
        return self._resistance


def main():
    """Create a resistor and read its resistance through the property."""
    r = Resistor("R1", 220)

    # Reading through the property works.
    print(r.resistance)   # 220

    # The internal attribute can still be changed directly because Python
    # does not enforce privacy. The underscore is a convention meaning
    # "treat this as internal."
    r._resistance = 330
    print(r.resistance)   # 330


if __name__ == "__main__":
    main()
