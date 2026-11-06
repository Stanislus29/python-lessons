class Resistor:
    def __init__(self, name, resistance):
        self.name = name
        self._resistance = resistance

    @property
    def resistance(self):
        return self._resistance

r = Resistor("R1", 220)
r._resistance = 330  # Update the resistance value
print(r.resistance)