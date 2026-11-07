"""
03_exercise_voltage.py
======================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Exercise 1: Processing electrical measurements
Section: C — Seven-minute student exercise (15–22 minutes)

What this does
--------------
Complete solution to Exercise 1. A measurement device records voltage values,
and the program applies several vectorized operations to the entire array
without using a for loop.

Students learn:
  * applying vectorized expressions to all elements of an array
  * multiplying, adding, squaring, and dividing arrays element-wise

Run it
------
    python 03_exercise_voltage.py
"""

import numpy as np

# A measurement device records the following voltage values.
voltage = np.array([2.0, 3.0, 4.0, 5.0, 6.0])

# 1. Multiply every measurement by 3.
print("Multiplied by 3:", voltage * 3)

# 2. Add 1.5 to every measurement.
print("Add 1.5:", voltage + 1.5)

# 3. Calculate the square of every measurement.
print("Squared:", voltage ** 2)

# 4. Divide every measurement by 2.
print("Divided by 2:", voltage / 2)

# Expected output:
#   Multiplied by 3: [ 6.  9. 12. 15. 18.]
#   Add 1.5: [3.5 4.5 5.5 6.5 7.5]
#   Squared: [ 4.  9. 16. 25. 36.]
#   Divided by 2: [1.  1.5 2.  2.5 3. ]
