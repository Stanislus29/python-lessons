"""
06_broadcasting.py
==================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Broadcasting
Section: D — Demonstration 3 (22–32 minutes)

What this does
--------------
Demonstrates broadcasting: NumPy performing operations between arrays of
compatible shapes without requiring the programmer to manually repeat values.

Students learn:
  * a scalar is applied to every element of an array
  * a one-dimensional array can be combined with a two-dimensional array
    when their dimensions are compatible
  * broadcasting applies values across rows/columns automatically

Run it
------
    python 06_broadcasting.py
"""

import numpy as np

# --- Broadcasting with a scalar --------------------------------------------

# A scalar value is applied to every element of the array.
readings = np.array([10, 20, 30, 40])
corrected = readings + 5
print("Scalar broadcasting:", corrected)
# Expected output: [15 25 35 45]

# --- Broadcasting with a two-dimensional array -----------------------------

measurements = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# A one-dimensional array with three elements, matching the three columns.
offsets = np.array([1, 2, 3])

# NumPy applies the offsets across each row.
corrected = measurements + offsets
print("2D broadcasting:")
print(corrected)
# Expected output:
#   [[11 22 33]
#    [41 52 63]
#    [71 82 93]]

# Explanation:
#   The one-dimensional offsets array is compatible with the three columns
#   of measurements. NumPy applies the offsets across each row.
#   Broadcasting allows certain operations between differently shaped arrays
#   when their dimensions are compatible.
