class Component:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        return f"{self.name}: {self.type}"

class Resistor(Component):
    def __init__(self, name, type, resistance):
        super().__init__(name, type)
        self._resistance = resistance

    def describe(self):
        base = super().describe()
        return f"{base}, {self._resistance} ohms"

r = Resistor("R1", "resistor", 220)
r._resistance = 330  # Update the resistance value
print(r.describe())