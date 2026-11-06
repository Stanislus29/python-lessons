#Model the Schokley Diode equation

def current(voltage, saturation_current, thermal_voltage):
    """
    Calculate the current through a Schokley diode given the voltage across it,
    the saturation current, and the thermal voltage.

    Parameters:
    voltage (float): The voltage across the diode (in volts).
    saturation_current (float): The saturation current of the diode (in amperes).
    thermal_voltage (float): The thermal voltage (in volts).

    Returns:
    float: The current through the diode (in amperes).
    """
    import math
    return saturation_current * (math.exp(voltage / thermal_voltage) - 1)

I = current(0.7, 1e-12, 0.025)  # Example values for voltage, saturation current, and thermal voltage
print(f"The current through the Schokley diode is: {I} A")