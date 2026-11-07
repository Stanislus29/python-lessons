# Python Numerical Computing: Vectorization with NumPy

**Institution:** Regent University College, Ghana  
**Instructor:** Stanislus E.-Onwuneme, Teaching Assistant (TA)  
**Duration:** 45 minutes  
**Topic:** Vectorization and array-based numerical computation  
**Prerequisite:** Basic Python syntax, loops, lists, and functions  
**Library:** NumPy

---

## 1. Lesson overview

This lesson introduces **vectorization**: expressing numerical operations on entire arrays instead of writing an explicit Python loop for every element. Students will move from ordinary Python list processing to NumPy array operations, then apply vectorization to filtering and simple sensor-data processing.

The central question for the lesson is:

> How can we perform calculations on an entire collection of numerical measurements without writing a separate Python operation for each value?

### Learning objectives

By the end of the lesson, students should be able to:

1. Explain what vectorization means in numerical computing.
2. Distinguish ordinary Python list behaviour from NumPy element-wise operations.
3. Perform arithmetic operations on NumPy arrays.
4. Use Boolean indexing to select values that satisfy a condition.
5. Use `np.where()` for element-wise conditional selection.
6. Explain and demonstrate basic broadcasting.
7. Apply vectorized operations to a small sensor-data problem.

### Lesson schedule

| Time | Section | Focus |
|---|---|---|
| 0–5 min | Introduction | Why vectorization matters |
| 5–15 min | Part 1 | Python loops versus NumPy vectorized operations |
| 15–22 min | Exercise 1 | Vectorized arithmetic |
| 22–32 min | Part 2 | Boolean indexing, `np.where()`, and broadcasting |
| 32–42 min | Practical application | Processing ADC sensor readings |
| 42–45 min | Exercise 2 and recap | Independent application |
| **Total** |  | **45 minutes** |

---

## 2. Teaching notes and demonstrations

## Section A — Introduction to vectorization (0–5 minutes)

### Opening question

Suppose a device records 1,000 numerical measurements. We need to multiply every measurement by two. How could we do this in Python?

Students may suggest a `for` loop. Use that answer to introduce two approaches:

- **Explicit iteration:** write a loop that visits each element and performs the operation.
- **Vectorized computation:** describe the operation once for an entire NumPy array.

### Explain the central idea

Vectorization allows a programmer to express an operation on an array as a whole. NumPy performs the element-wise numerical work internally, generally using compiled implementations rather than requiring the programmer to write a Python-level loop for each element.

Emphasise that vectorization does not mean the computer performs no iteration internally. It means the programmer can express the operation at the array level. This often reduces Python overhead and makes numerical code clearer.

### Introduce NumPy

```python
import numpy as np
```

NumPy is a Python library for working with numerical arrays and performing mathematical operations on them. Its central array object is called an `ndarray`.

---

## Section B — Python loops versus NumPy operations (5–15 minutes)

### Demonstration 1: Process a Python list with a loop

Start with an ordinary Python list:

```python
measurements = [10, 20, 30, 40, 50]

result = []

for value in measurements:
    result.append(value * 2)

print(result)
```

**Output:**

```text
[20, 40, 60, 80, 100]
```

Explain the process:

1. The loop retrieves one value from the list.
2. Python multiplies that value by two.
3. The result is appended to a new list.
4. The loop repeats until every value has been processed.

### Demonstration 2: Perform the same operation with NumPy

```python
import numpy as np

measurements = np.array([10, 20, 30, 40, 50])

result = measurements * 2

print(result)
```

**Output:**

```text
[ 20  40  60  80 100]
```

Explain that `measurements * 2` applies multiplication to every element in the array. There is no explicit Python loop in the code.

### Demonstration 3: Other element-wise arithmetic operations

```python
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 6, 8])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square of a:", a ** 2)
```

**Output:**

```text
Addition: [12 24 36 48]
Subtraction: [ 8 16 24 32]
Multiplication: [ 20  80 180 320]
Division: [5. 5. 5. 5.]
Square of a: [ 100  400  900 1600]
```

### Teaching points

- NumPy arithmetic is element-wise when the operation is applied to arrays of compatible shapes.
- In this example, `a` and `b` have the same shape, so corresponding elements are paired.
- `a * b` is element-wise multiplication. It is not matrix multiplication.
- NumPy commonly returns an array of numerical results. The displayed formatting may differ from a Python list.

**Check for understanding:** Ask students what `a + 10` would do. It adds 10 to every element; this is also an example of broadcasting, which is covered later.

---

## Section C — Seven-minute student exercise (15–22 minutes)

### Exercise 1: Processing electrical measurements

A measurement device records the following voltage values:

```python
voltage = np.array([2.0, 3.0, 4.0, 5.0, 6.0])
```

Ask students to write NumPy expressions to:

1. Multiply every measurement by 3.
2. Add 1.5 to every measurement.
3. Calculate the square of every measurement.
4. Divide every measurement by 2.

**Instruction:** Students should use vectorized expressions rather than writing a `for` loop.

### Expected solution

```python
import numpy as np

voltage = np.array([2.0, 3.0, 4.0, 5.0, 6.0])

print("Multiplied by 3:", voltage * 3)
print("Add 1.5:", voltage + 1.5)
print("Squared:", voltage ** 2)
print("Divided by 2:", voltage / 2)
```

**Expected output:**

```text
Multiplied by 3: [ 6.  9. 12. 15. 18.]
Add 1.5: [3.5 4.5 5.5 6.5 7.5]
Squared: [ 4.  9. 16. 25. 36.]
Divided by 2: [1.  1.5 2.  2.5 3. ]
```

### Instructor guidance

Look for whether students understand that the operation is applied to all elements. Correct any solution that uses list repetition or concatenation instead of numerical multiplication.

---

## Section D — Logical vectorization and broadcasting (22–32 minutes)

This section extends vectorization beyond arithmetic. NumPy can also evaluate conditions across arrays and apply compatible operations to arrays with different shapes.

### Demonstration 1: Boolean indexing

Suppose we have a collection of temperature readings:

```python
temperature = np.array([22, 25, 28, 31, 34, 29, 20])
```

We want to select all readings greater than 28.

```python
high_temperature = temperature[temperature > 28]

print(high_temperature)
```

**Output:**

```text
[31 34 29]
```

Break the expression into two steps:

```python
condition = temperature > 28
print(condition)
```

**Output:**

```text
[False False False  True  True  True False]
```

Explain:

- `temperature > 28` compares every element with 28.
- The comparison produces a Boolean array containing `True` or `False` values.
- `temperature[condition]` selects the elements whose corresponding condition is `True`.

This is called **Boolean indexing** or Boolean masking.

### Demonstration 2: Conditional operations with `np.where()`

Suppose we want to classify each temperature reading as either `High` or `Normal`.

```python
temperature = np.array([22, 25, 28, 31, 34])

status = np.where(
    temperature > 28,
    "High",
    "Normal"
)

print(status)
```

**Output:**

```text
['Normal' 'Normal' 'Normal' 'High' 'High']
```

Explain the structure:

```python
np.where(condition, value_if_true, value_if_false)
```

`np.where()` evaluates the condition element by element and chooses the corresponding output value.

### Demonstration 3: Broadcasting

Broadcasting allows NumPy to perform operations between arrays of compatible shapes without requiring the programmer to manually repeat values.

Start with a scalar:

```python
readings = np.array([10, 20, 30, 40])

corrected = readings + 5

print(corrected)
```

**Output:**

```text
[15 25 35 45]
```

Explain that the scalar `5` is applied to every element.

Now demonstrate broadcasting with a two-dimensional array:

```python
measurements = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

offsets = np.array([1, 2, 3])

corrected = measurements + offsets

print(corrected)
```

**Output:**

```text
[[11 22 33]
 [41 52 63]
 [71 82 93]]
```

Explain that the one-dimensional `offsets` array is compatible with the three columns of `measurements`. NumPy applies the offsets across each row.

**Keep the explanation introductory:** Students only need to understand that broadcasting allows certain operations between differently shaped arrays when their dimensions are compatible. More detailed broadcasting rules can be addressed in a later class.

---

## Section E — Practical application: Sensor data processing (32–42 minutes)

### Problem: Converting ADC readings into voltage

A microcontroller records sensor measurements using a 12-bit analogue-to-digital converter (ADC). The ADC uses a reference voltage of 3.3 V.

Suppose the recorded digital values are:

```python
raw_data = np.array([
    0, 450, 900, 1350, 1800,
    2250, 2700, 3150, 3600, 4095
])
```

A 12-bit ADC represents values from 0 to 4095 because:

\[
2^{12} = 4096
\]

Using the common endpoint-scaling convention, convert the digital reading into voltage with:

\[
V = \frac{ADC \times V_{ref}}{4095}
\]

where:

- \(V\) is the estimated input voltage.
- \(ADC\) is the digital reading.
- \(V_{ref}\) is the reference voltage, 3.3 V.

### Demonstration 1: Convert every reading into voltage

```python
import numpy as np

raw_data = np.array([
    0, 450, 900, 1350, 1800,
    2250, 2700, 3150, 3600, 4095
])

voltage = raw_data * (3.3 / 4095)

print(voltage)
```

**Expected output (rounded for display):**

```text
[0.         0.36263736 0.72527473 1.08791209 1.45054945
 1.81318681 2.17582418 2.53846154 2.9010989  3.3       ]
```

Point out that one expression converts the entire array. No explicit loop is required.

### Demonstration 2: Select readings above a threshold

Suppose we want to identify converted readings above 2 volts.

```python
high_readings = voltage[voltage > 2.0]

print(high_readings)
```

**Expected output:**

```text
[2.17582418 2.53846154 2.9010989  3.3       ]
```

Explain that Boolean indexing selects only values satisfying the condition. The comparison uses a strict greater-than test, so a value equal to 2.0 would not be selected.

### Demonstration 3: Calculate basic statistics

```python
print("Average voltage:", np.mean(voltage))
print("Maximum voltage:", np.max(voltage))
print("Minimum voltage:", np.min(voltage))
```

These functions calculate summary information from the array:

| Function | Purpose |
|---|---|
| `np.mean()` | Calculates the arithmetic average |
| `np.max()` | Returns the largest value |
| `np.min()` | Returns the smallest value |

### Demonstration 4: Calculate changes between consecutive readings

```python
changes = np.diff(voltage)

print(changes)
```

`np.diff()` calculates the difference between each pair of consecutive values. For example, the first result is the second reading minus the first reading.

This can help reveal changes in sensor measurements over time. It does not, by itself, calculate a rate of change; a time interval is also needed to calculate a rate.

### Bring the demonstration together

Ask students to identify which NumPy operations were used:

- Arithmetic vectorization: `raw_data * (3.3 / 4095)`
- Boolean indexing: `voltage[voltage > 2.0]`
- Statistical operations: `np.mean()`, `np.max()`, and `np.min()`
- Difference between consecutive values: `np.diff()`

---

## Section F — Final exercise and recap (42–45 minutes)

### Exercise 2: Basic sensor-data analysis

Students are given the following readings:

```python
readings = np.array([100, 200, 300, 400, 500])
```

Ask them to:

1. Convert the readings using a scale factor of `0.01`.
2. Select converted readings strictly greater than 3.
3. Calculate the average of the converted readings.

### Expected solution

```python
import numpy as np

readings = np.array([100, 200, 300, 400, 500])

voltage = readings * 0.01
high_readings = voltage[voltage > 3]
average = np.mean(voltage)

print("Converted readings:", voltage)
print("Readings above 3:", high_readings)
print("Average:", average)
```

**Expected output:**

```text
Converted readings: [1. 2. 3. 4. 5.]
Readings above 3: [4. 5.]
Average: 3.0
```

### Final recap

Ask students to explain these five ideas in their own words:

| Concept | Key idea |
|---|---|
| Python loops | Explicitly process elements one at a time |
| Vectorized arithmetic | Apply numerical operations across arrays |
| Boolean indexing | Select elements using a condition |
| `np.where()` | Choose values based on an element-wise condition |
| Broadcasting | Apply operations between arrays with compatible shapes |

Close with the central takeaway:

> Vectorization lets us express numerical operations on entire datasets. It makes numerical code more concise and can make many array computations more efficient by reducing Python-level loop overhead.

---

## 3. Common mistakes to watch for

1. **Confusing list repetition with numerical multiplication.** In Python, `[1, 2] * 2` repeats the list. In NumPy, `np.array([1, 2]) * 2` multiplies each element by two.
2. **Confusing element-wise multiplication with matrix multiplication.** `A * B` is element-wise multiplication. For matrix multiplication, NumPy uses `A @ B` or `np.matmul(A, B)`.
3. **Using incompatible shapes.** Not every pair of arrays can be combined through broadcasting. The dimensions must be compatible.
4. **Misreading Boolean indexing.** `array > threshold` produces a Boolean array; using it inside `array[...]` selects the matching values.
5. **Assuming `np.where()` filters an array.** It selects between output values based on a condition. Boolean indexing is generally the more direct choice when the goal is to return only matching elements.
6. **Overstating performance gains.** Vectorization often improves performance for numerical workloads, but the benefit depends on the operation, array size and implementation. Its clearest introductory advantage is expressing operations at the array level.

## 4. Instructor preparation checklist

Before class:

- [ ] Confirm NumPy is installed in the Python environment (`python -m pip install numpy` if needed).
- [ ] Test the code examples in a Python interpreter or notebook.
- [ ] Ensure students can run a Python script and import a library.
- [ ] Keep the ADC example visible while explaining the conversion formula.
- [ ] Allow students to attempt both exercises before showing the solutions.

## 5. Suggested transition to the next lesson

This lecture introduces vectorization as a way to operate on numerical arrays. The next stage can apply these ideas to **vector mathematics and applied linear algebra**, including vector magnitudes, dot products, matrix transformations and coordinate operations.

These topics will form part of **Part 2: Applied Numerical Computing** in the wider Python course.
