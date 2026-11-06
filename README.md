# Python Teaching Examples

Regent University College, Accra, Ghana

This repository contains Python scripts and lecture materials I used for two
class sessions:

* **Regular session** — weekday classes (`regular/`)
* **Weekend session** — weekend classes (`weekend/`)

A separate **Encapsulation** topic (`encapsulation/`) supplements both
sessions with object-oriented programming material.

## Purpose

These are teaching examples for students learning Python. Each script is
self-contained, heavily commented, and written so that students can read it,
run it, and experiment with it. File names describe what each script does.

## Repository layout

```
regular/          Regular (weekday) session
  01_basics/      Variables, arithmetic, functions, lists, conditionals, dicts
  02_electronics/ Voltage divider, Shockley diode, NumPy intro
  03_oop/         Classes, inheritance, polymorphism (+ lecture slides)

weekend/          Weekend session
  01_basics/      Input, conditionals, charge calculation, even numbers
  02_oop/         Capacitor class

encapsulation/    Encapsulation and @property (getter/setter, validation)
```

## Getting started

See **USAGE.md** for guidelines on how to run the scripts, what you need
installed, and how students and instructors should use this repository.

## Requirements

* Python 3 (tested with Python 3.14)
* NumPy (only for `regular/02_electronics/numpy_matrix_intro.py`)

```bash
pip install numpy
```

## License

Teaching material — free to use and adapt for classes.
