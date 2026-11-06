"""
simple_functions.py
===================
Regent University College, Accra, Ghana
Python for Beginners - Regular Session
Topic: Defining and calling functions

What this does
--------------
Defines two small functions, add() and multiply(), that perform basic
arithmetic and return their results. A main() function runs examples and
prints the answers.

Students learn:
  * how to define a function with def
  * how to pass arguments (parameters) to a function
  * how to return a value with return
  * the if __name__ == "__main__" guard that runs the demo only when
    this file is executed directly (not when imported)

Run it
------
    python simple_functions.py
"""


def add(x, y):
    """Return the sum of x and y."""
    z = x + y
    return z


def multiply(x, y):
    """Return the product of x and y."""
    z = x * y
    return z


def main():
    """Run example calculations and print the results."""
    z = add(3, 2)          # 3 + 2 = 5
    p = multiply(5, 7)     # 5 * 7 = 35
    print('Answer is:', z)
    print('Answer is:', p)


# Only run main() when this file is executed directly.
# Importing this file in another script will NOT run the examples.
if __name__ == "__main__":
    main()
