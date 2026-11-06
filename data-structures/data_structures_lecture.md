# Python Class: Data Structures — Lists and Dictionaries

**Duration:** 45 minutes  
**Audience:** Beginner Python learners  
**Format:** Short explanations, live coding, guided examples, and student practice

> **Timing note:** The requested list sequence (10 minutes of teaching, a 7-minute exercise, then 10 more minutes on lists) uses 27 minutes after the introduction. To fit dictionaries into the remaining 13 minutes, this plan gives dictionaries a 10-minute teaching block and a 3-minute mini-exercise. A full 7-minute dictionary exercise would make the class 49 minutes; a full 10 + 7 + 10 dictionary sequence would make it 59 minutes.

## Learning objectives

By the end of the class, students should be able to:

1. Explain what a data structure is and why programs use them.
2. Create, access, update, and loop through a Python list.
3. Use common list methods such as `append()`, `remove()`, and `sort()`.
4. Create, access, update, and loop through a Python dictionary.
5. Choose between a list and a dictionary for a simple programming task.

## Materials and preparation

- A computer with Python 3 installed.
- A code editor or Python interactive shell.
- A screen/projector for live coding, if available.

Before class, check that Python runs and that students can execute a `.py` file. Ask students to follow along with the examples rather than copy everything silently.

---

# Lesson schedule

| Time | Duration | Segment |
|---|---:|---|
| 00:00–00:05 | 5 min | Introduction to data structures |
| 00:05–00:15 | 10 min | Lists: concepts and example programs |
| 00:15–00:22 | 7 min | Student exercise: lists |
| 00:22–00:32 | 10 min | More on lists: useful operations and a practical program |
| 00:32–00:42 | 10 min | Dictionaries: concepts and example program |
| 00:42–00:45 | 3 min | Student mini-exercise: dictionaries and closing check |
| **Total** | **45 min** | |

---

## 1. Introduction to data structures (5 minutes)

### Teaching goal

Introduce the idea that programs often need to store and organise more than one piece of information.

### Explain

A **data structure** is a way of organising data so a program can store, access, and work with it.

Start with a simple example. A program that stores one student's score could use a variable:

```python
score = 85
```

But what if the program needs to store the scores of five students? Creating a separate variable for every score quickly becomes inconvenient. A data structure lets us keep related values together.

Today, focus on two built-in Python data structures:

- **List:** stores an ordered collection of items.
- **Dictionary:** stores information as key-value pairs.

### Opening question

Ask: **“If we were writing a program to store the names of everyone in this class, would it be convenient to create one variable for every student?”**

Use their answers to introduce collections.

---

## 2. Lists: concepts and example programs (10 minutes)

### Teaching goal

Show students how to create a list and retrieve items from it.

### Explain the key ideas

A list:

- is written using square brackets: `[]`;
- can contain multiple values;
- keeps items in order;
- uses zero-based indexing, so the first item is at index `0`;
- can be changed after it is created.

### Example 1: Create and access a list

```python
students = ["Ama", "Kojo", "Esi", "Yaw"]

print(students)
print(students[0])  # First item
print(students[2])  # Third item
print(len(students))  # Number of items
```

**Ask students:** Why does `students[0]` return `"Ama"` rather than `"Kojo"`?

Emphasise that Python starts counting list positions from zero.

### Example 2: Loop through a list

```python
students = ["Ama", "Kojo", "Esi", "Yaw"]

for student in students:
    print(student)
```

Explain that a `for` loop can visit each item in the list. The variable `student` takes the value of the current item on each iteration.

### Example 3: Add an item to a list

```python
students = ["Ama", "Kojo", "Esi"]

students.append("Yaw")

print(students)
```

Explain that `append()` adds one item to the end of a list.

### Quick check

Ask students to predict the output before running this:

```python
numbers = [4, 8, 12]
print(numbers[1])
```

**Expected output:** `8`

---

## 3. Student exercise: lists (7 minutes)

### Task: Manage a shopping list

Ask students to write a program that:

1. Creates a list containing three items: `"Rice"`, `"Eggs"`, and `"Tomatoes"`.
2. Prints the list.
3. Adds `"Milk"` to the list.
4. Prints the updated list.
5. Prints the second item in the list.

**Starter code:**

```python
shopping_list = ["Rice", "Eggs", "Tomatoes"]

# Print the original list

# Add "Milk"

# Print the updated list

# Print the second item
```

### Expected result

```text
['Rice', 'Eggs', 'Tomatoes']
['Rice', 'Eggs', 'Tomatoes', 'Milk']
Eggs
```

### Instructor guidance

Give students a few minutes to work independently, then ask one student to explain how they used `append()` and indexing. If students get stuck, remind them that the second item is at index `1`.

---

## 4. More on lists: useful operations and a practical program (10 minutes)

### Teaching goal

Move beyond creating and reading lists. Demonstrate how to modify, inspect, and process their contents.

### Useful list operations

```python
numbers = [7, 2, 9, 4]

numbers.append(6)       # Add 6 to the end
numbers.remove(2)       # Remove the first matching 2
numbers.sort()          # Sort the list in ascending order

print(numbers)
print(len(numbers))     # Number of items
print(sum(numbers))     # Sum of numeric items
```

Discuss these operations:

| Operation | Purpose |
|---|---|
| `append(item)` | Adds an item to the end |
| `remove(item)` | Removes the first matching item |
| `sort()` | Sorts the list in place |
| `len(my_list)` | Returns the number of items |
| `sum(my_list)` | Adds numeric items together |

Point out that `remove()` expects a value, while indexing uses a position.

### Practical example: Calculate the average score

```python
scores = [75, 82, 68, 90, 85]

total = sum(scores)
number_of_students = len(scores)
average = total / number_of_students

print("Total score:", total)
print("Number of students:", number_of_students)
print("Average score:", average)
```

### Explain the program

1. `scores` stores the students' scores in one list.
2. `sum(scores)` adds all the scores.
3. `len(scores)` counts the number of scores.
4. Dividing the total by the count gives the average.

Ask students what would happen if another score were added to the list before the calculation. The average would update automatically because the program uses `sum()` and `len()` rather than fixed values.

### Optional extension if the class is moving quickly

Ask students to print only scores greater than or equal to `80`:

```python
scores = [75, 82, 68, 90, 85]

for score in scores:
    if score >= 80:
        print(score)
```

---

## 5. Dictionaries: concepts and example program (10 minutes)

### Teaching goal

Introduce key-value storage and show when it is more useful than a list.

### Explain the key ideas

A **dictionary** stores information as **key-value pairs**. Each key is used to look up its associated value.

A dictionary:

- is written using curly braces: `{}`;
- stores pairs in the form `key: value`;
- is useful when values have labels, such as a student's name, age, or score;
- is accessed using keys rather than numeric positions.

### Example 1: Create and access a dictionary

```python
student = {
    "name": "Ama",
    "age": 19,
    "score": 85
}

print(student["name"])
print(student["score"])
```

Explain that `"name"` and `"score"` are keys. Their associated values are `"Ama"` and `85`.

### Example 2: Add and update information

```python
student = {
    "name": "Ama",
    "age": 19,
    "score": 85
}

student["course"] = "Computer Engineering"  # Add a new pair
student["score"] = 90                       # Update an existing value

print(student)
```

Explain the difference:

- Assigning a value to a new key adds a key-value pair.
- Assigning a value to an existing key changes that key's value.

### Example 3: Loop through a dictionary

```python
student = {
    "name": "Ama",
    "age": 19,
    "score": 90
}

for key, value in student.items():
    print(key, ":", value)
```

Explain that `.items()` allows the loop to access each key and its corresponding value.

### A useful detail: `get()`

Using square brackets for a key that does not exist raises a `KeyError`. The `get()` method provides a default value instead:

```python
student = {"name": "Ama", "score": 90}

print(student.get("course", "Not provided"))
```

**Expected output:** `Not provided`

---

## 6. Student mini-exercise: dictionaries and closing check (3 minutes)

### Task: Store a student's details

Ask students to create a dictionary named `student` with these pairs:

- `"name"`: `"Kojo"`
- `"age"`: `20`
- `"score"`: `78`

Then ask them to:

1. Print the student's name.
2. Update the score to `88`.
3. Print the updated dictionary.

**Starter code:**

```python
student = {
    # Add the three key-value pairs here
}

# Print the student's name

# Update the score

# Print the dictionary
```

### Expected solution

```python
student = {
    "name": "Kojo",
    "age": 20,
    "score": 78
}

print(student["name"])
student["score"] = 88
print(student)
```

### Closing check

Ask students these two questions:

1. Which structure would you use to store a simple sequence of five scores? **A list.**
2. Which structure would you use to store one student's name, age, and score under meaningful labels? **A dictionary.**

Conclude with the central distinction: **lists organise values by position; dictionaries organise values by key.**

---

# Instructor answer key at a glance

| Exercise | Main concepts being checked |
|---|---|
| Shopping list | List creation, `print()`, `append()`, indexing |
| Student record | Dictionary creation, key lookup, updating a value |

## Common mistakes to watch for

- **Using the wrong index:** The first list item is at index `0`, not `1`.
- **Using parentheses instead of square brackets:** List indexing looks like `students[0]`.
- **Forgetting quotation marks:** String values and string dictionary keys need quotation marks.
- **Confusing a key with a position:** `student["name"]` looks up a dictionary key; `students[0]` accesses a list position.
- **Misspelling a dictionary key:** Keys must match exactly, including capitalisation.

## Final comparison

| Feature | List | Dictionary |
|---|---|---|
| Syntax | `[]` | `{}` |
| Stores | Ordered items | Key-value pairs |
| Access | By index, e.g. `items[0]` | By key, e.g. `record["name"]` |
| Example use | Scores, names, shopping items | Student profile, product details |

**Take-home practice:** Create a list containing the names of three subjects. Then create a dictionary for one subject with the keys `"name"`, `"teacher"`, and `"room"`. Print the list and each value in the dictionary.
