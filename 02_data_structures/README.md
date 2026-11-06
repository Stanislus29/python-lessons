# 02_data_structures — Lists and Dictionaries

Regent University College, Accra, Ghana

This folder teaches how to store and organise collections of data using
Python's two most important built-in data structures: **lists** and
**dictionaries**.

## Concepts covered

* Creating lists with `[]` and accessing items by index (zero-based)
* Looping through lists with `for`
* Adding items to lists with `append()`
* List methods: `remove()`, `sort()`, `len()`, `sum()`
* Creating dictionaries with `{}` and accessing values by key
* Adding and updating dictionary entries
* Looping through dictionaries with `.items()`
* Using `.get()` for safe lookups with default values

## Scripts

| # | File | What it does |
|---|------|--------------|
| 1 | `01_single_score.py` | Stores one score in a variable; motivates data structures |
| 2 | `02_create_access_list.py` | Creates a list and accesses items by index |
| 3 | `03_loop_through_list.py` | Loops through a list and prints each item |
| 4 | `04_add_item_to_list.py` | Adds an item to a list with `append()` |
| 5 | `05_quick_check_index.py` | Prints the item at index 1 (expected output: 8) |
| 6 | `06_shopping_list.py` | Shopping list exercise: create, append, print, index |
| 7 | `07_list_operations.py` | `append()`, `remove()`, `sort()`, `len()`, `sum()` |
| 8 | `08_average_score.py` | Calculates the average score of a list |
| 9 | `09_scores_above_80.py` | Prints scores >= 80 using a loop and `if` |
| 10 | `10_create_access_dict.py` | Creates a dictionary and looks up values by key |
| 11 | `11_add_update_dict.py` | Adds a new pair and updates an existing value |
| 12 | `12_loop_through_dict.py` | Loops through a dictionary with `.items()` |
| 13 | `13_dict_get_method.py` | Uses `get()` with a default for a missing key |
| 14 | `14_student_details.py` | Student details: create, lookup, update, print |
| 15 | `15_take_home_practice.py` | Subject list + subject dictionary (take-home practice) |
| — | `component_inventory.py` | List of capacitor dictionaries; computes charge and sorts |
| — | `dictionaries.py` | Stores capacitors in a dictionary; computes charge `Q = C * V` |
| — | `working_with_lists.py` | Demonstrates `append()`, `insert()`, `pop()` on a list |

## Lecture material

| File | What it is |
|------|------------|
| `data_structures_lecture.md` | 45-minute lecture plan on lists and dictionaries |
| `python_data_structures_slides.pptx` | Slides for the data structures lecture |

## How to run

```bash
cd 02_data_structures
python 06_shopping_list.py
```

## Next steps

After understanding data structures, move on to **03_functions** to learn how
to write reusable blocks of code.
