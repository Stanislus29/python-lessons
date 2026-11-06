# 02_electronics — Electronics Applications

Regent University College, Accra, Ghana
Regular session

## What this folder covers

Real-world electronics formulas written in Python: voltage dividers, the
Shockley diode equation, and an introduction to NumPy arrays.

## Files

| File | What it does |
|------|--------------|
| `voltage_divider_functions.py` | Voltage divider using plain functions |
| `voltage_divider_class.py` | Voltage divider using a class (`VDiv`) |
| `shockley_diode.py` | Shockley diode equation `I = Is * (e^(V/Vt) - 1)` |
| `numpy_matrix_intro.py` | Creates a 2x2 NumPy matrix; prints shape and size |

## Prerequisites

The NumPy script requires NumPy:

```bash
pip install numpy
```

## How to run

```bash
cd regular/02_electronics
python voltage_divider_functions.py
```

The class version (`voltage_divider_class.py`) covers the same formulas as
the functions version, but bundles data and behaviour into a class — useful
for comparing procedural and object-oriented styles.
