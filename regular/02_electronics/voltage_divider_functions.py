"""
voltage_divider_functions.py
============================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Electronics application - voltage divider (using functions)

What this does
--------------
Models a resistor voltage divider using plain functions. A voltage divider
produces a lower output voltage (Vout) from a higher input voltage (Vin)
using two resistors, R1 and R2:

    Vout = Vin * R2 / (R1 + R2)

The program provides three functions:
  * voltage_divider(vin, r1, r2)   - compute Vout
  * resistor_combination(vout, vin, r2)  - find R1 for a desired Vout
  * divider_ratio(vout, vin)       - compute the Vout/Vin ratio

A main() block demonstrates each function with example values.

Students learn:
  * writing functions that take parameters and return values
  * applying a real-world electronics formula in code
  * formatted floating-point output with f-strings (:.2f)

Run it
------
    python voltage_divider_functions.py
"""


def voltage_divider(vin, r1, r2):
    """Return the output voltage of a divider: Vout = Vin * R2 / (R1 + R2)."""
    vout = vin * (r2 / (r1 + r2))
    return vout


def resistor_combination(vout, vin, r2):
    """Return R1 needed to produce vout, given vin and r2.

    Rearranged from the divider formula: R1 = (R2 * Vin / Vout) - R2.
    """
    r1 = (r2 * vin / vout) - r2
    return r1


def divider_ratio(vout, vin):
    """Return the ratio Vout / Vin."""
    ratio = vout / vin
    return ratio


def main():
    """Run example calculations and print the results."""
    ratio = divider_ratio(3, 5)
    print(f"The ratio of Vout to Vin is: {ratio:.2f}")

    r1 = resistor_combination(3, 5, 5000)
    print(f"The value of R1 is: {r1:.2f} ohms")

    vout = voltage_divider(5, 5000, 1000)
    print(f"The output voltage (Vout) is: {vout:.2f} V")


if __name__ == "__main__":
    main()
