"""
07_adc_conversion.py
====================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — ADC sensor data conversion
Section: E — Practical application: Sensor data processing (32–42 minutes)

What this does
--------------
Converts 12-bit ADC (analogue-to-digital converter) readings into voltage
using a single vectorized expression. A 12-bit ADC represents values from
0 to 4095 (2^12 = 4096), and the reference voltage is 3.3 V.

Conversion formula (endpoint-scaling convention):

    V = (ADC × V_ref) / 4095

Students learn:
  * converting an entire array of ADC readings into voltage with one expression
  * no explicit loop is required for vectorized computation

Run it
------
    python 07_adc_conversion.py
"""

import numpy as np

# Recorded digital values from a 12-bit ADC (0 to 4095).
raw_data = np.array([
    0, 450, 900, 1350, 1800,
    2250, 2700, 3150, 3600, 4095
])

# Reference voltage of the ADC.
v_ref = 3.3

# Convert every reading into voltage using a single vectorized expression.
# V = (ADC × V_ref) / 4095
voltage = raw_data * (v_ref / 4095)

print("Voltage readings:")
print(voltage)
# Expected output (rounded for display):
#   [0.         0.36263736 0.72527473 1.08791209 1.45054945
#    1.81318681 2.17582418 2.53846154 2.9010989  3.3       ]

# Explanation:
#   One expression converts the entire array. No explicit loop is required.
#   This is the core advantage of vectorization: express the operation at
#   the array level.
