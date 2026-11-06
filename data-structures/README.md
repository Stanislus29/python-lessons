# Data Structures — Lists and Dictionaries

Regent University College, Accra, Ghana

This folder contains runnable Python scripts extracted from the lesson plan
`data_structures_lecture.md` (45-minute class on lists and dictionaries).
Each script is numbered in the order it appears in the lesson and includes
comments explaining what it does.

## Scripts

| # | File | Lesson section | What it does |
|---|------|----------------|--------------|
| 1 | `01_single_score.py` | 1. Introduction | Stores one score in a variable; motivates data structures |
| 2 | `02_create_access_list.py` | 2. Lists — Example 1 | Creates a list and accesses items by index |
| 3 | `03_loop_through_list.py` | 2. Lists — Example 2 | Loops through a list and prints each item |
| 4 | `04_add_item_to_list.py` | 2. Lists — Example 3 | Adds an item to a list with append() |
| 5 | `05_quick_check_index.py` | 2. Lists — Quick check | Prints the item at index 1 (expected: 8) |
| 6 | `06_shopping_list.py` | 3. Exercise: lists | Shopping list: create, append, print, index |
| 7 | `07_list_operations.py` | 4. Lists — operations | append(), remove(), sort(), len(), sum() |
| 8 | `08_average_score.py` | 4. Lists — average | Calculates the average score of a list |
| 9 | `09_scores_above_80.py` | 4. Lists — extension | Prints scores >= 80 using a loop and if |
| 10 | `10_create_access_dict.py` | 5. Dicts — Example 1 | Creates a dictionary and looks up values by key |
| 11 | `11_add_update_dict.py` | 5. Dicts — Example 2 | Adds a new pair and updates an existing value |
| 12 | `12_loop_through_dict.py` | 5. Dicts — Example 3 | Loops through a dictionary with .items() |
| 13 | `13_dict_get_method.py` | 5. Dicts — get() | Uses get() with a default for a missing key |
| 14 | `14_student_details.py` | 6. Exercise: dicts | Student details: create, lookup, update, print |
| 15 | `15_take_home_practice.py` | Take-home practice | List of subjects + subject dictionary |

## How to run

From the repository root:

```bash
cd data-structures
python 01_single_score.py
python 06_shopping_list.py
```

Each script is self-contained and can be run independently.

## Source lesson plan

The full lesson plan (objectives, schedule, exercises, expected answers, and
common mistakes) lives at:

```
regular/01_basics/data_structures_lecture.md
```
