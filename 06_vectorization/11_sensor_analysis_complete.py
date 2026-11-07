"""
11_sensor_analysis_complete.py
==============================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Complete sensor data analysis
Section: E — Bring the demonstration together (32–42 minutes)

What this does
--------------
Brings together all the NumPy operations demonstrated in the sensor data
processing section: ADC conversion, Boolean indexing, statistics, and
consecutive differences.

Students learn:
  * combining multiple vectorized operations into one analysis script
  * identifying which NumPy operations were used at each step

Run it
------
    python 11_sensor_analysis_complete.py
"""

import numpy as np

# Recorded digital values from a 12-bit ADC (0 to 4095).
raw_data = np.array([
    0, 450, 900, 1350, 1800,
    2250, 2700, 3150, 3600, 4095
])

# Reference voltage of the ADC.
v_ref = 3.3

# --- Step 1: Convert every reading into voltage ----------------------------
# Arithmetic vectorization: raw_data * (3.3 / 4095)
voltage = raw_data * (v_ref / 4095)
print("Converted voltage readings:")
print(voltage)

# --- Step 2: Select readings above a threshold -----------------------------
# Boolean indexing: voltage[voltage > 2.0]
high_readings = voltage[voltage > 2.0]
print("\nReadings above 2.0 V:")
print(high_readings)

# --- Step 3: Calculate basic statistics ------------------------------------
# Statistical operations: np.mean(), np.max(), np.min()
print("\nAverage voltage:", np.mean(voltage))
print("Maximum voltage:", np.max(voltage))
print("Minimum voltage:", np.min(voltage))

# --- Step 4: Calculate changes between consecutive readings -----------------
# Difference between consecutive values: np.diff()
changes = np.diff(voltage)
print("\nChanges between consecutive readings:")
print(changes)

# Summary of NumPy operations used:
#   - Arithmetic vectorization: raw_data * (3.3 / 4095)
#   - Boolean indexing: voltage[voltage > 2.0]
#   - Statistical operations: np.mean(), np.max(), np.min()
#   - Difference between consecutive values: np.diff()
