"""
component_inventory.py
======================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Lists of dictionaries, sorting, and formatted output

What this does
--------------
Keeps an inventory of capacitors as a list of dictionaries. Each dictionary
holds the capacitor type and its capacitance. The program computes the charge
stored on each capacitor at a fixed voltage, sorts the capacitors by charge
(highest first), and prints a tidy table.

Students learn:
  * lists of dictionaries
  * adding a new key to each dictionary in a loop
  * sorted() with a lambda key function
  * formatted strings with f-strings and alignment (:<12)

Run it
------
    python component_inventory.py
"""

# Fixed supply voltage (in volts).
V = 12

# Inventory: each capacitor is a dictionary with 'type' and 'capacitance'.
capacitors = [
    {"type": "electrolytic", "capacitance": 5e-6},
    {"type": "electrolytic", "capacitance": 50e-12},
    {"type": "electrolytic", "capacitance": 500e-12},
    {"type": "ceramic", "capacitance": 1e-9},
    {"type": "ceramic", "capacitance": 10e-9},
]

# Compute and store the charge Q = C * V on each capacitor.
for cap in capacitors:
    cap["charge"] = cap["capacitance"] * V

# Sort by charge, highest charge first (reverse=True).
sorted_capacitors = sorted(capacitors, key=lambda x: x["charge"], reverse=True)

print("\nSorted Capacitors by Charge (highest first):")
for cap in sorted_capacitors:
    print(
        f"Type: {cap['type']:<12}, "
        f"Capacitance: {cap['capacitance']} F, "
        f"Charge: {cap['charge']} C"
    )
