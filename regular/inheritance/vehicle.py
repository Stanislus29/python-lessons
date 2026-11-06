class Vehicle:
    def __init__(self, make,top_speed):
        self.make = make
        self.top_speed = top_speed

    def describe(self):
        return f"{self.make}: {self.top_speed} km/h"

class Motorcycle(Vehicle):
    def __init__(self, make, top_speed, has_sidecar = False):
        super().__init__(make, top_speed)
        self.has_sidecar = has_sidecar

    def describe(self):
        base = super().describe()
        sidecar_status = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base}, {sidecar_status}"

vehicle = Vehicle("Toyota", 180)
motorcycle = Motorcycle("Harley-Davidson", 200, True)
print(vehicle.describe())  # Output: Toyota: 180 km/h
print(motorcycle.describe())  # Output: Harley-Davidson: 200 km/h,