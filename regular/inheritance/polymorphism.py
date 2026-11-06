class Component:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        return f"{self.name}: {self.type}"

class Resistor(Component):
    def __init__(self, name, type, resistance):
        super().__init__(name, type)
        self.resistance = resistance

    def describe(self):
        base = super().describe()
        return f"{base}, {self.resistance} ohms"

class Capacitor(Component):
    def __init__(self, name, type, capacitance, usage):
        super().__init__(name, type)
        self.capacitance = capacitance
        self.usage = usage

    def describe(self):
        base = super().describe()
        return f"{base}, {self.capacitance} farads, {self.usage}"

component = [Resistor("R1", "resistor", 220), Capacitor("C1", "capacitor", 1000, "filter")]

for c in component:
    print(c.describe())