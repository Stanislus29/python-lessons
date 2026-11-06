"""
vehicle_inheritance.py
======================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Object-Oriented Programming - inheritance with vehicles

What this does
--------------
Defines a base class Vehicle with a make and top speed, and a subclass
Motorcycle that inherits from Vehicle and adds whether it has a sidecar.
Both classes have a describe() method; Motorcycle overrides describe() to
include the sidecar information.

Students learn:
  * inheritance: class Motorcycle(Vehicle)
  * calling the parent constructor with super().__init__()
  * overriding a method in a subclass
  * isinstance checks (every Motorcycle is a Vehicle)

Run it
------
    python vehicle_inheritance.py
"""


class Vehicle:
    """A generic vehicle with a make and a top speed.

    Attributes:
        make (str): The manufacturer of the vehicle.
        top_speed (int or float): Top speed in km/h.
    """

    def __init__(self, make, top_speed):
        """Initialise the vehicle with its make and top speed."""
        self.make = make
        self.top_speed = top_speed

    def describe(self):
        """Return a short description of the vehicle."""
        return f"{self.make}: {self.top_speed} km/h"


class Motorcycle(Vehicle):
    """A motorcycle: a Vehicle that may or may not have a sidecar.

    Attributes:
        make (str): inherited from Vehicle
        top_speed (int or float): inherited from Vehicle
        has_sidecar (bool): whether the motorcycle has a sidecar
    """

    def __init__(self, make, top_speed, has_sidecar=False):
        """Initialise the motorcycle; has_sidecar defaults to False."""
        # Let Vehicle handle make and top_speed.
        super().__init__(make, top_speed)
        self.has_sidecar = has_sidecar

    def describe(self):
        """Return a description including sidecar status."""
        base = super().describe()   # start with the parent's description
        sidecar_status = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base}, {sidecar_status}"


def main():
    """Create a vehicle and a motorcycle and describe both."""
    vehicle = Vehicle("Toyota", 180)
    motorcycle = Motorcycle("Harley-Davidson", 200, True)

    print(vehicle.describe())   # Toyota: 180 km/h
    print(motorcycle.describe())  # Harley-Davidson: 200 km/h, with sidecar

    # Demonstrate that a Motorcycle is also a Vehicle.
    print("Is motorcycle a Vehicle?", isinstance(motorcycle, Vehicle))


if __name__ == "__main__":
    main()
