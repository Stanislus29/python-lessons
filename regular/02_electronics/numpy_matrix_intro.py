"""
numpy_matrix_intro.py
=====================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Introduction to NumPy arrays and matrices

What this does
--------------
Creates a 2x2 matrix (a two-dimensional NumPy array) and prints it along
with its shape (number of rows and columns) and size (total number of
elements).

Students learn:
  * importing NumPy with import numpy as np
  * creating a NumPy array from a nested Python list
  * reading the .shape and .size attributes of an array

Prerequisites
-------------
This script requires NumPy. Install it with:
    pip install numpy

Run it
------
    python numpy_matrix_intro.py
"""

import numpy as np

# Create a 2x2 matrix (two rows, two columns).
matrix = np.array([[1, 2],
                   [3, 4]])

print("Matrix:")
print(matrix)

print("Shape of the matrix (rows, columns):", matrix.shape)
print("Size of the matrix (total elements):", matrix.size)
