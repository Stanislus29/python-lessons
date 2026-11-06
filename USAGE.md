# Guidelines for Usage

Regent University College, Accra, Ghana

This document explains how students and instructors should use the Python
teaching examples in this repository.

## 1. Who this is for

* **Students:** work through the folders in order, starting with
  `01_intro_basics`. Each script is a standalone example with comments
  explaining what it does.
* **Instructors:** use the scripts as live-coding demos or in-class
  exercises. Each folder has its own README with a topic guide, and some
  folders include lecture plans and slide files.

## 2. Suggested progression

Work through the folders in this order:

| Order | Folder | What you'll learn |
|-------|--------|-------------------|
| 1 | `01_intro_basics/` | Variables, arithmetic, input, conditionals |
| 2 | `02_data_structures/` | Lists and dictionaries |
| 3 | `03_functions/` | Defining and calling functions |
| 4 | `04_object_oriented/` | Classes, inheritance, polymorphism, encapsulation |
| 5 | `05_applications_electronics/` | Real-world electronics applications |

## 3. Prerequisites

Install Python 3. For the NumPy demo you also need NumPy:

```bash
pip install numpy
```

No other packages are required.

## 4. How to run a script

Open a terminal, go to the folder that contains the script you want, and run
it with Python:

```bash
# Example: introduction
cd 01_intro_basics
python hello_addition.py

# Example: data structures
cd 02_data_structures
python 06_shopping_list.py

# Example: object-oriented programming
cd 04_object_oriented
python student_records.py

# Example: electronics application
cd 05_applications_electronics
python voltage_divider_functions.py
```

Each script includes an `if __name__ == "__main__":` block, so the example
only runs when you execute the file directly. Importing a file into another
script will not run its demo code.

## 5. Folder conventions

Each folder is numbered to show the suggested learning order. File names
describe what each script does (for example,
`voltage_divider_class.py` shows a voltage divider built with a class).

## 6. For students

* Run every script and observe the output.
* Change the numbers and text in the scripts to see what happens.
* Read the comments — they explain each line in plain language.
* Try writing your own small script based on each example before moving to
  the next folder.

## 7. For instructors

* Each folder has its own `README.md` with a short topic guide and script
  descriptions.
* Lecture plans are included as Markdown files:
  * `02_data_structures/data_structures_lecture.md` — 45-minute lecture on
    lists and dictionaries
  * `04_object_oriented/inheritance_lecture.md` — 45-minute lecture on
    Python inheritance
* Slide files (`.pptx`) are in `02_data_structures/` and `04_object_oriented/`.

## 8. Contributing changes

If you fix a bug, improve a comment, or add a new example:

1. Place the file in the folder matching its concept level.
2. Give the file a name that says what it does.
3. Add a module docstring and line comments so students can follow along.
4. Run the script to confirm it works before sharing it.

## 9. What to avoid

* Do not commit `__pycache__/` folders or `.pyc` files (they are generated
  automatically — see `.gitignore`).
* Do not commit virtual-environment folders (`.venv/`).
* Avoid shadowing built-in names (for example, do not name a variable
  `list`).
