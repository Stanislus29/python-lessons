"""
shockley_diode.py
=================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Electronics application - Shockley diode equation

What this does
--------------
Models the current through a diode using the Shockley diode equation:

    I = Is * (e^(V / Vt) - 1)

where:
  * I   is the diode current (amperes)
  * Is  is the saturation current (amperes)
  * V   is the voltage across the diode (volts)
  * Vt  is the thermal voltage (volts)

The program calculates an example current and prints it.

Students learn:
  * using math.exp() for the exponential function
  * writing a function with parameters and a return value
  * importing the math module
  * applying a physics/electronics formula in code

Run it
------
    python shockley_diode.py
"""

import math


def current(voltage, saturation_current, thermal_voltage):
    """Calculate the diode current using the Shockley diode equation.

    I = Is * (e^(V / Vt) - 1)

    Parameters:
        voltage (float): Voltage across the diode (volts).
        saturation_current (float): Saturation current of the diode (amperes).
        thermal_voltage (float): Thermal voltage (volts).

    Returns:
        float: Current through the diode (amperes).
    """
    return saturation_current * (math.exp(voltage / thermal_voltage) - 1)


# Example calculation with typical values.
# V = 0.7 V, Is = 1e-12 A, Vt = 0.025 V
diode_voltage = 0.7
saturation_current = 1e-12
thermal_voltage = 0.025

diode_current = current(diode_voltage, saturation_current, thermal_voltage)

print(f"The current through the Shockley diode is: {diode_current} A")
