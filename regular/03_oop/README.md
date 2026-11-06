# 03_oop — Object-Oriented Programming

Regent University College, Accra, Ghana
Regular session

## What this folder covers

Classes, objects, inheritance, method overriding, `super()`, and
polymorphism.

## Files

| File | What it does |
|------|--------------|
| `student_records.py` | A `Student` class with name, age, grade, and `add_points()` |
| `dog_class.py` | A `Dog` class with `name`, `age`, and a `bark()` method |
| `using_dog_class.py` | Imports `Dog` and adds a `GuideDog` subclass (inheritance) |
| `vehicle_inheritance.py` | `Vehicle` base class and `Motorcycle` subclass with `super()` |
| `component_and_resistor.py` | `Component` base class and `Resistor` subclass (inheritance + `_attribute` convention) |
| `polymorphism.py` | Mixed list of `Resistor` and `Capacitor` objects; one `describe()` call works for all |

## Lecture materials

| File | What it is |
|------|------------|
| `inheritance_lecture.md` | 45-minute lecture plan on inheritance (live code, exercises, homework) |
| `python_classes_slides.pptx` | Slides for the classes lecture |
| `python_inheritance_slides.pptx` | Slides for the inheritance lecture |

## How to run

```bash
cd regular/03_oop
python student_records.py
```

Note: `using_dog_class.py` imports `dog_class.py`, so run it from the
`03_oop/` folder so the import resolves.
