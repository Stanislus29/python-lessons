"""
capacitor_charge.py
===================
Regent University College, Accra, Ghana
Python for Beginners - Weekend Session
Topic: Functions, lists, and a simple electronics calculation

What this does
--------------
Stores a list of capacitance values and, for each one, computes the charge
stored using Q = C * V at a fixed voltage of 10 volts. It then prints the
charge and flags whether each result is "ok" (above 5) or "not ok".

Students learn:
  * defining a function that takes parameters and returns a value
  * looping over a list of numbers
  * scientific notation for small values (e.g. 5e-12)
  * if / else to categorise results
  * formatted output with f-strings (:.2f)

Run it
------
    python capacitor_charge.py
"""

# Capacitance values in farads (scientific notation: 5e-12 = 0.000000000005 F).
capacitances = [5e-12, 10e-6, 100e-9]


def charge(c, v):
    """Return the charge Q = C * V (in coulombs)."""
    q = c * v
    return q


# Fixed voltage for every calculation (in volts).
voltage = 10

# Compute and report the charge on each capacitor.
for c in capacitances:
    a = charge(c, voltage)   # charge on this capacitor
    print(a)

    if a > 5:
        print(f"ok:{a:.2f}")
    else:
        print(f"Not ok:{a:.2f}")
