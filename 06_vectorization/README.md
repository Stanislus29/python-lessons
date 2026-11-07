# 06_vectorization — Vectorization with NumPy

Regent University College, Accra, Ghana  
Department of Engineering · Level 200 (L200)

This folder teaches **vectorization**: expressing numerical operations on
entire arrays instead of writing an explicit Python loop for every element.
It builds on the NumPy introduction in `05_applications_electronics/`.

## Concepts covered

* Python loops versus NumPy vectorized operations
* Element-wise arithmetic on NumPy arrays
* Boolean indexing (Boolean masking)
* `np.where()` for element-wise conditional selection
* Broadcasting (scalar and array)
* Applying vectorized operations to ADC sensor data
* Summary statistics: `np.mean()`, `np.max()`, `np.min()`
* `np.diff()` for changes between consecutive readings

## Scripts

| # | File | Lesson section | What it does |
|---|------|----------------|--------------|
| 1 | `01_python_loop_vs_numpy.py` | B — Demo 1 & 2 | List with for loop vs NumPy array without a loop |
| 2 | `02_element_wise_arithmetic.py` | B — Demo 3 | Add, subtract, multiply, divide, square arrays |
| 3 | `03_exercise_voltage.py` | C — Exercise 1 | Vectorized operations on voltage measurements |
| 4 | `04_boolean_indexing.py` | D — Demo 1 | Select elements using a Boolean condition |
| 5 | `05_np_where.py` | D — Demo 2 | Choose values with `np.where(condition, true, false)` |
| 6 | `06_broadcasting.py` | D — Demo 3 | Scalar and 2D array broadcasting |
| 7 | `07_adc_conversion.py` | E — Demo 1 | Convert 12-bit ADC readings to voltage |
| 8 | `08_high_readings.py` | E — Demo 2 | Select voltage readings above a threshold |
| 9 | `09_statistics.py` | E — Demo 3 | Mean, max, min of an array |
| 10 | `10_diff_changes.py` | E — Demo 4 | Differences between consecutive readings |
| 11 | `11_sensor_analysis_complete.py` | E — Combined | Complete ADC sensor analysis |
| 12 | `12_exercise_sensor_analysis.py` | F — Exercise 2 | Convert, filter, and average sensor readings |

## Lecture material

| File | What it is |
|------|------------|
| `python_vectorization_45_min_lecture.md` | 45-minute lecture plan on vectorization with NumPy |
| `python_vectorization_regent_slides.pptx` | Slides for the vectorization lecture |

## Prerequisites

NumPy is required:

```bash
pip install numpy
```

## How to run

```bash
cd 06_vectorization
python 01_python_loop_vs_numpy.py
python 07_adc_conversion.py
```

## Suggested progression

Work through the folders in order:

1. `01_intro_basics/` — variables, arithmetic, input, conditionals
2. `02_data_structures/` — lists and dictionaries
3. `03_functions/` — defining and calling functions
4. `04_object_oriented/` — classes, inheritance, polymorphism, encapsulation
5. `05_applications_electronics/` — real-world electronics applications
6. `06_vectorization/` — vectorized numerical computing with NumPy
