V = 12

capacitors = [
    {"type": "electrolytic", "capacitance": 5e-6},
    {"type": "electrolytic", "capacitance": 50e-12},  
    {"type": "electrolytic", "capacitance": 500e-12},  
    {"type": "ceramic", "capacitance": 1e-9},
    {"type": "ceramic", "capacitance": 10e-9},
]


for cap in capacitors:
    cap["charge"] = cap["capacitance"] * V

sorted_capacitors = sorted(capacitors, key=lambda x: x["charge"], reverse = True)

print("\nSorted Capacitors by Capacitance:")
for cap in sorted_capacitors:
    print(f"Type: {cap['type']:<12}, Capacitance: {cap['capacitance']} F, Charge: {cap['charge']} C")