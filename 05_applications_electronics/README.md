# 05_applications_electronics — Real-World Applications

Regent University College, Accra, Ghana

This folder brings together everything learned in the previous folders and
applies Python to real-world electronics problems. These scripts combine
variables, functions, data structures, and object-oriented programming to
solve practical engineering calculations.

## Concepts covered

* Applying physics and electronics formulas in code
* Voltage divider: `Vout = Vin * R2 / (R1 + R2)`
* Shockley diode equation: `I = Is * (e^(V/Vt) - 1)`
* NumPy arrays and matrices for numerical work
* Object-oriented voltage divider calculator (`VDiv` class)
* Capacitor charge calculation: `Q = C * V`

## Scripts

| File | What it does |
|------|--------------|
| `voltage_divider_functions.py` | Voltage divider using plain functions |
| `voltage_divider_class.py` | Voltage divider using a class (`VDiv`) — OOP version of the functions script |
| `shockley_diode.py` | Shockley diode equation `I = Is * (e^(V/Vt) - 1)` |
| `numpy_matrix_intro.py` | Creates a 2x2 NumPy matrix; prints shape and size |
| `capacitor_charge.py` | Computes charge `Q = C * V` for capacitors; flags results above/below 5 |

## Prerequisites

The NumPy script requires NumPy:

```bash
pip install numpy
```

## How to run

```bash
cd 05_applications_electronics
python voltage_divider_functions.py
```

## Suggested progression

Work through the folders in order:

1. **01_intro_basics** — variables, arithmetic, input, conditionals
2. **02_data_structures** — lists and dictionaries
3. **03_functions** — reusable code blocks
4. **04_object_oriented** — classes, inheritance, polymorphism, encapsulation
5. **05_applications_electronics** — real-world electronics applications
