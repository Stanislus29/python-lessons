#class to calculate the charge stored in a capacitor

class Capacitor:
    def __init__(self, capacitance, voltage):
        self.capacitance = capacitance
        self.voltage = voltage

    def charge(self):
        return self.capacitance * self.voltage

c1 = Capacitor(5e-12, 10)
print(f"Charge stored in capacitor 1: {c1.charge():.2e} C")