"""
08_high_readings.py
===================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Selecting readings above a threshold
Section: E — Demonstration 2 (32–42 minutes)

What this does
--------------
Uses Boolean indexing to identify converted voltage readings that exceed
a threshold of 2 volts.

Students learn:
  * using array[array > threshold] to select values satisfying a condition
  * strict greater-than means a value equal to the threshold is excluded

Run it
------
    python 08_high_readings.py
"""

import numpy as np

# Converted voltage readings from the ADC conversion example.
voltage = np.array([
    0.0, 0.36263736, 0.72527473, 1.08791209, 1.45054945,
    1.81318681, 2.17582418, 2.53846154, 2.9010989, 3.3
])

# Identify converted readings above 2 volts.
high_readings = voltage[voltage > 2.0]

print("Readings above 2.0 V:")
print(high_readings)
# Expected output: [2.17582418 2.53846154 2.9010989  3.3       ]

# Explanation:
#   Boolean indexing selects only values satisfying the condition.
#   The comparison uses a strict greater-than test, so a value equal to
#   2.0 would not be selected.
