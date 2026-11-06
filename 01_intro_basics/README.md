# 01_intro_basics — Introduction to Python

Regent University College, Accra, Ghana

This is the starting point of the Python teaching progression. These scripts
cover the absolute basics: variables, arithmetic, reading user input, and
conditional logic. No prior programming knowledge is assumed.

## Concepts covered

* Variables and assignment
* Arithmetic operators (`+`, `-`, `*`, `/`, `%`)
* Reading input from the keyboard with `input()`
* Converting input to numbers with `int()`
* Conditional statements: `if`, `elif`, `else`
* Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`

## Scripts

| File | What it does |
|------|--------------|
| `hello_addition.py` | Stores two numbers, adds them, prints the result |
| `arithmetic_with_input.py` | Reads two numbers from the user; prints sum, product, quotient; checks for a factor |
| `adult_or_minor.py` | Reads an age and prints "adult" (18+) or "minor" |
| `conditionals.py` | Loops through numbers and tests a condition with `if` / `break` |
| `even_numbers.py` | Loops through numbers and reports the even ones |

## How to run

```bash
cd 01_intro_basics
python hello_addition.py
```

Scripts that use `input()` will wait for you to type a value and press Enter.

## Next steps

After mastering these basics, move on to **02_data_structures** to learn how
to store collections of data with lists and dictionaries.
