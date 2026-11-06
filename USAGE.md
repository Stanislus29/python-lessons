# Guidelines for Usage

Regent University College, Accra, Ghana

This document explains how students and instructors should use the Python
teaching examples in this repository.

## 1. Who this is for

* **Students:** read and run the scripts to follow along with class. Each
  file is a standalone example with comments explaining what it does.
* **Instructors:** use the scripts as live-coding demos or in-class
  exercises. Session-by-session notes are in each folder's README.

## 2. Prerequisites

Install Python 3. For the NumPy demo you also need NumPy:

```bash
pip install numpy
```

No other packages are required.

## 3. How to run a script

Open a terminal, go to the folder that contains the script you want, and run
it with Python:

```bash
# Example: regular session, basics
cd regular/01_basics
python hello_addition.py

# Example: weekend session, basics
cd weekend/01_basics
python adult_or_minor.py
```

Each script includes an `if __name__ == "__main__":` block, so the example
only runs when you execute the file directly. Importing a file into another
script will not run its demo code.

## 4. Folder conventions

| Folder | What it contains |
|--------|------------------|
| `regular/01_basics/` | Core Python: variables, functions, lists, conditionals, dictionaries |
| `regular/02_electronics/` | Electronics applications: voltage divider, Shockley diode, NumPy |
| `regular/03_oop/` | Object-oriented programming: classes, inheritance, polymorphism |
| `weekend/01_basics/` | Core Python for the weekend session |
| `weekend/02_oop/` | Object-oriented programming for the weekend session |
| `encapsulation/` | Encapsulation with `@property` (read-only and validated) |

File names describe what each script does (for example,
`voltage_divider_class.py` shows a voltage divider built with a class).

## 5. For students

* Run every script and observe the output.
* Change the numbers and text in the scripts to see what happens.
* Read the comments — they explain each line in plain language.
* Try writing your own small script based on each example before the next
  class.

## 6. For instructors

* Each session folder has its own `README.md` with a short topic guide.
* The file `regular/03_oop/inheritance_lecture.md` is a 45-minute lecture
  plan on Python inheritance, including timeline, live-code examples,
  exercises, common mistakes, and homework.
* Slide files (`.pptx`) are in `regular/03_oop/`.

## 7. Contributing changes

If you fix a bug, improve a comment, or add a new example:

1. Give the file a name that says what it does.
2. Add a module docstring and line comments so students can follow along.
3. Run the script to confirm it works before sharing it.

## 8. What to avoid

* Do not commit `__pycache__/` folders or `.pyc` files (they are generated
  automatically — see `.gitignore`).
* Do not commit virtual-environment folders (`.venv/`).
* Avoid shadowing built-in names (for example, do not name a variable
  `list`).
