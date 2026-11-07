"""
05_np_where.py
==============
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — np.where() conditional selection
Section: D — Demonstration 2 (22–32 minutes)

What this does
--------------
Demonstrates np.where() for element-wise conditional selection: choosing
between two output values based on a condition evaluated across an array.

Students learn:
  * np.where(condition, value_if_true, value_if_false)
  * np.where evaluates the condition element by element
  * np.where selects between output values (it does not filter an array)

Run it
------
    python 05_np_where.py
"""

import numpy as np

# A collection of temperature readings.
temperature = np.array([22, 25, 28, 31, 34])

# Classify each reading as "High" or "Normal" based on a threshold of 28.
status = np.where(
    temperature > 28,
    "High",
    "Normal"
)

print("Status:", status)
# Expected output: ['Normal' 'Normal' 'Normal' 'High' 'High']

# Explanation:
#   np.where() evaluates the condition element by element and chooses the
#   corresponding output value ("High" or "Normal") for each position.
#   Note: np.where() selects between output values based on a condition.
#   Boolean indexing (temperature[temperature > 28]) is generally the more
#   direct choice when the goal is to return only matching elements.
