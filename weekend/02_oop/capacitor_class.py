"""
capacitor_class.py
==================
Regent University College, Accra, Ghana
Python for Beginners - Weekend Session
Topic: Object-Oriented Programming - a Capacitor class

What this does
--------------
Defines a Capacitor class that stores a capacitance and a voltage, with a
charge() method that computes the stored charge Q = C * V. It creates one
capacitor and prints the charge it stores.

Students learn:
  * defining a class with __init__ and self
  * storing data as object attributes (capacitance, voltage)
  * defining a method that computes a value from the object's data
  * creating an instance and calling its method
  * formatted scientific output with :.2e

Run it
------
    python capacitor_class.py
"""


class Capacitor:
    """Represents a capacitor that stores charge.

    Attributes:
        capacitance (float): Capacitance in farads.
        voltage (float): Voltage across the capacitor in volts.
    """

    def __init__(self, capacitance, voltage):
        """Initialise the capacitor with its capacitance and voltage."""
        self.capacitance = capacitance
        self.voltage = voltage

    def charge(self):
        """Return the stored charge Q = C * V (in coulombs)."""
        return self.capacitance * self.voltage


def main():
    """Create a capacitor and print the charge it stores."""
    # 5 picofarads at 10 volts.
    c1 = Capacitor(5e-12, 10)
    print(f"Charge stored in capacitor 1: {c1.charge():.2e} C")


if __name__ == "__main__":
    main()
