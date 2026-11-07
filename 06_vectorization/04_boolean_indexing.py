"""
04_boolean_indexing.py
======================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Boolean indexing
Section: D — Demonstration 1 (22–32 minutes)

What this does
--------------
Demonstrates Boolean indexing (Boolean masking): selecting array elements
that satisfy a condition by using a Boolean array as an index.

Students learn:
  * comparing every element with a value produces a Boolean array
  * using array[condition] selects elements where the condition is True
  * this is called Boolean indexing or Boolean masking

Run it
------
    python 04_boolean_indexing.py
"""

import numpy as np

# A collection of temperature readings.
temperature = np.array([22, 25, 28, 31, 34, 29, 20])

# Step 1: Compare every element with 28. This produces a Boolean array.
condition = temperature > 28
print("Condition array:", condition)
# Expected output: [False False False  True  True  True False]

# Step 2: Select elements whose corresponding condition is True.
high_temperature = temperature[condition]
print("High temperatures:", high_temperature)
# Expected output: [31 34 29]

# Equivalent one-liner:
#   high_temperature = temperature[temperature > 28]

# Explanation:
#   * temperature > 28 compares every element with 28.
#   * The comparison produces True or False for each element.
#   * temperature[condition] selects only elements where the condition is True.
