"""
12_exercise_sensor_analysis.py
==============================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Exercise 2: Basic sensor-data analysis
Section: F — Final exercise and recap (42–45 minutes)

What this does
--------------
Complete solution to Exercise 2. Given a set of raw readings, the program:
  1. converts the readings using a scale factor of 0.01,
  2. selects converted readings strictly greater than 3,
  3. calculates the average of the converted readings.

Students learn:
  * applying vectorized conversion, filtering, and statistics in sequence

Run it
------
    python 12_exercise_sensor_analysis.py
"""

import numpy as np

# Given readings.
readings = np.array([100, 200, 300, 400, 500])

# 1. Convert the readings using a scale factor of 0.01.
voltage = readings * 0.01

# 2. Select converted readings strictly greater than 3.
high_readings = voltage[voltage > 3]

# 3. Calculate the average of the converted readings.
average = np.mean(voltage)

print("Converted readings:", voltage)
print("Readings above 3:", high_readings)
print("Average:", average)

# Expected output:
#   Converted readings: [1. 2. 3. 4. 5.]
#   Readings above 3: [4. 5.]
#   Average: 3.0
