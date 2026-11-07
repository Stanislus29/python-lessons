"""
02_element_wise_arithmetic.py
=============================
Regent University College, Accra, Ghana
Department of Engineering · Level 200 (L200)
Topic: Vectorization with NumPy — Element-wise arithmetic
Section: B — Demonstration 3 (5–15 minutes)

What this does
--------------
Shows element-wise arithmetic operations on NumPy arrays: addition,
subtraction, multiplication, division, and exponentiation.

Students learn:
  * NumPy arithmetic is element-wise for arrays of compatible shapes
  * a * b is element-wise multiplication (not matrix multiplication)
  * corresponding elements are paired when arrays have the same shape

Run it
------
    python 02_element_wise_arithmetic.py
"""

import numpy as np

# Two arrays with the same shape.
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 6, 8])

# Element-wise arithmetic operations.
print("Addition:", a + b)        # [12 24 36 48]
print("Subtraction:", a - b)    # [ 8 16 24 32]
print("Multiplication:", a * b) # [ 20  80 180 320]
print("Division:", a / b)       # [5. 5. 5. 5.]
print("Square of a:", a ** 2)   # [ 100  400  900 1600]

# Teaching points:
#   * NumPy arithmetic is element-wise when arrays have compatible shapes.
#   * a and b have the same shape, so corresponding elements are paired.
#   * a * b is element-wise multiplication, NOT matrix multiplication.
#   * For matrix multiplication, use A @ B or np.matmul(A, B).
