"""
09_statistics.py
================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Basic statistics on arrays
Section: E — Demonstration 3 (32–42 minutes)

What this does
--------------
Calculates summary statistics (average, maximum, minimum) for a NumPy
array of voltage readings using np.mean(), np.max(), and np.min().

Students learn:
  * np.mean() calculates the arithmetic average
  * np.max() returns the largest value
  * np.min() returns the smallest value

Run it
------
    python 09_statistics.py
"""

import numpy as np

# Converted voltage readings from the ADC conversion example.
voltage = np.array([
    0.0, 0.36263736, 0.72527473, 1.08791209, 1.45054945,
    1.81318681, 2.17582418, 2.53846154, 2.9010989, 3.3
])

# Calculate summary statistics from the array.
print("Average voltage:", np.mean(voltage))
print("Maximum voltage:", np.max(voltage))
print("Minimum voltage:", np.min(voltage))

# Expected output:
#   Average voltage: 1.82457803...
#   Maximum voltage: 3.3
#   Minimum voltage: 0.0

# Explanation:
#   These functions calculate summary information from the entire array:
#   | Function | Purpose                              |
#   | np.mean()  | Calculates the arithmetic average    |
#   | np.max()   | Returns the largest value            |
#   | np.min()   | Returns the smallest value           |
