class Resistor:
    def __init__(self, name, resistance):
        self.name = name
        self._resistance = resistance

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, value):
        if value <= 0:
            raise ValueError("resistance must be positive")
        self._resistance = value

r = Resistor("R1", 220)
r.resistance = 330
print(r.resistance)

r.resistance = -50