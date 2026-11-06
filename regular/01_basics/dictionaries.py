"""
dictionaries.py
===============
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Dictionaries and a simple electronics calculation

What this does
--------------
Stores a dictionary of capacitor types, where each type maps to a list of
capacitance values. For every capacitor it computes the stored charge using

    Q = C * V

(charge equals capacitance times voltage) and prints the result.

Students learn:
  * creating and iterating over a dictionary
  * nested iteration (dictionary items, then a list of values)
  * defining and calling a simple function

Run it
------
    python dictionaries.py
"""

# Mapping from capacitor type -> list of capacitance values (in farads).
# Scientific notation like 5e-6 means 5 * 10^-6 = 0.000005 F.
components = {
    "electrolytic": [5e-6, 50e-12, 500e-12],
    "ceramic": [1e-9, 10e-9],
}

# Supply voltage used for every charge calculation (in volts).
voltage = 1200


def charge(capacitance, voltage):
    """Return the charge Q = C * V (in coulombs)."""
    return capacitance * voltage


# Loop over each capacitor type and its list of capacitance values.
for component_type, capacitances in components.items():
    for capacitance in capacitances:
        q = charge(capacitance, voltage)
        print(f"{component_type}: C = {capacitance} F, Q = {q} C")
