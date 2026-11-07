"""
01_python_loop_vs_numpy.py
==========================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Python loops vs NumPy operations
Section: B — Python loops versus NumPy operations (5–15 minutes)

What this does
--------------
Demonstrates the difference between processing a Python list with an
explicit for loop and performing the same operation with a NumPy array
using vectorized computation.

Students learn:
  * how to process a list element by element with a for loop and append()
  * how to perform the same operation on a NumPy array without a loop
  * that NumPy vectorization expresses the operation at the array level

Run it
------
    python 01_python_loop_vs_numpy.py
"""

# --- Demonstration 1: Process a Python list with a loop ---------------------

# Start with an ordinary Python list of measurements.
measurements = [10, 20, 30, 40, 50]

# Prepare an empty list to hold the results.
result = []

# Visit each value, multiply by two, and append to the result list.
for value in measurements:
    result.append(value * 2)

print("Python loop result:", result)
# Expected output: [20, 40, 60, 80, 100]

# --- Demonstration 2: Perform the same operation with NumPy -----------------

import numpy as np

# Create a NumPy array from the same values.
measurements = np.array([10, 20, 30, 40, 50])

# Apply multiplication to every element at once. No explicit Python loop.
result = measurements * 2

print("NumPy result:", result)
# Expected output: [ 20  40  60  80 100]

# Explanation:
#   measurements * 2 applies multiplication to every element in the array.
#   There is no explicit Python loop in the code. NumPy performs the
#   element-wise numerical work internally.
