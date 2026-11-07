"""
10_diff_changes.py
==================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Changes between consecutive readings
Section: E — Demonstration 4 (32–42 minutes)

What this does
--------------
Calculates the difference between each pair of consecutive voltage readings
using np.diff(). This helps reveal changes in sensor measurements over time.

Students learn:
  * np.diff() calculates the difference between consecutive values
  * the first result is the second reading minus the first reading
  * np.diff() does not calculate a rate of change (a time interval is needed
    for that)

Run it
------
    python 10_diff_changes.py
"""

import numpy as np

# Converted voltage readings from the ADC conversion example.
voltage = np.array([
    0.0, 0.36263736, 0.72527473, 1.08791209, 1.45054945,
    1.81318681, 2.17582418, 2.53846154, 2.9010989, 3.3
])

# Calculate the difference between each pair of consecutive values.
changes = np.diff(voltage)

print("Changes between consecutive readings:")
print(changes)

# Explanation:
#   np.diff() calculates the difference between each pair of consecutive
#   values. For example, the first result is the second reading minus the
#   first reading.
#   This can help reveal changes in sensor measurements over time. It does
#   not, by itself, calculate a rate of change; a time interval is also
#   needed to calculate a rate.
