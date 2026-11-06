"""
validated_property.py
=====================
Regent University College, Accra, Ghana
Python for Beginners - Topic: Encapsulation with a validated setter

What this does
--------------
Defines a Resistor class with a resistance that is exposed through a
@property and can be changed through a @resistance.setter. The setter
validates the value and raises a ValueError if the resistance is not
positive, preventing invalid data from entering the object.

This demonstrates full encapsulation: controlling both reading and
writing of an attribute, with validation.

Students learn:
  * the @property decorator (getter)
  * the @<name>.setter decorator (setter)
  * raising ValueError to reject invalid input
  * using try / except to handle the error gracefully

Run it
------
    python validated_property.py
"""


class Resistor:
    """A resistor with a validated, positive resistance value.

    Attributes:
        name (str): The resistor's name.
        _resistance (float): Internal resistance in ohms (must be > 0).
    """

    def __init__(self, name, resistance):
        """Initialise the resistor; the setter validates the resistance."""
        self.name = name
        self.resistance = resistance   # goes through the setter below

    @property
    def resistance(self):
        """Return the resistance value."""
        return self._resistance

    @resistance.setter
    def resistance(self, value):
        """Set the resistance, rejecting values that are not positive."""
        if value <= 0:
            raise ValueError("resistance must be positive")
        self._resistance = value


def main():
    """Create a resistor, change its resistance, and try an invalid value."""
    r = Resistor("R1", 220)

    # Valid change goes through the setter.
    r.resistance = 330
    print(r.resistance)   # 330

    # Invalid change (<= 0) raises ValueError; we catch it to show
    # students what happens rather than crashing the program.
    try:
        r.resistance = -50
    except ValueError as error:
        print("Caught an error:", error)


if __name__ == "__main__":
    main()
