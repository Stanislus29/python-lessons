"""
voltage_divider_class.py
========================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Electronics application - voltage divider (using a class)

What this does
--------------
Models a resistor voltage divider using an object-oriented approach. The
VDiv class stores the input voltage and the two resistor values, and
provides methods to:

  * compute the output voltage (voltage_divider)
  * find R1 for a desired output voltage (resistor_combination)
  * compute the Vout/Vin ratio (divider_ratio)

A main() block demonstrates the class with example values.

This is the object-oriented version of voltage_divider_functions.py. It
shows how to bundle related data (vin, r1, r2) and behaviour (methods)
into a single class.

Students learn:
  * defining a class with __init__ (the constructor)
  * using self to access an object's own data
  * calling methods on an object
  * the if __name__ == "__main__" guard

Run it
------
    python voltage_divider_class.py
"""


class VDiv:
    """A resistor voltage divider calculator.

    Attributes:
        vin (float): Input voltage in volts.
        r1 (float): First resistor value in ohms.
        r2 (float): Second resistor value in ohms.
    """

    def __init__(self, vin, r1, r2):
        """Initialise the divider with Vin, R1 and R2."""
        self.vin = vin
        self.r1 = r1
        self.r2 = r2

    def voltage_divider(self):
        """Return the output voltage: Vout = Vin * R2 / (R1 + R2)."""
        vout = self.vin * (self.r2 / (self.r1 + self.r2))
        return vout

    def resistor_combination(self, vout):
        """Return R1 needed to produce the given vout.

        Rearranged from the divider formula: R1 = (R2 * Vin / Vout) - R2.
        """
        r1 = (self.r2 * self.vin / vout) - self.r2
        return r1

    def divider_ratio(self, vout):
        """Return the ratio Vout / Vin for the given vout."""
        ratio = vout / self.vin
        return ratio


def main():
    """Run example calculations using the VDiv class and print results."""
    calculator = VDiv(5, 5000, 1000)   # Vin=5V, R1=5k, R2=1k

    ratio = calculator.divider_ratio(4.2)
    print(f"The ratio of Vout to Vin is: {ratio:.2f}")

    r1 = calculator.resistor_combination(4.2)
    print(f"The value of R1 is: {r1:.2f} ohms")

    vout = calculator.voltage_divider()
    print(f"The output voltage (Vout) is: {vout:.2f} V")


# Only run the demo when this file is executed directly.
if __name__ == "__main__":
    main()
