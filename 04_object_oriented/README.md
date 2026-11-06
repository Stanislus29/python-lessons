# 04_object_oriented — Object-Oriented Programming

Regent University College, Accra, Ghana

This folder teaches object-oriented programming (OOP): how to define classes,
create objects, use inheritance, override methods, and control access to
object data through encapsulation.

## Concepts covered

* Defining a class with `class`
* The `__init__` constructor and `self`
* Storing data as object attributes
* Defining and calling methods on objects
* Creating multiple instances of the same class
* Inheritance: `class Child(Parent)`
* Calling the parent constructor with `super().__init__()`
* Overriding methods in a subclass
* Polymorphism: treating different objects uniformly through a shared method
* Encapsulation with `@property` (getter) and `@<name>.setter` (setter)
* Validating data before storing it in an object
* The underscore convention (`_attribute`) for internal attributes

## Scripts

| File | What it does |
|------|--------------|
| `student_records.py` | A `Student` class with name, age, grade, and `add_points()` |
| `dog_class.py` | A `Dog` class with `name`, `age`, and a `bark()` method |
| `using_dog_class.py` | Imports `Dog` and adds a `GuideDog` subclass (inheritance) |
| `vehicle_inheritance.py` | `Vehicle` base class and `Motorcycle` subclass with `super()` |
| `component_and_resistor.py` | `Component` base class and `Resistor` subclass (inheritance + `_attribute` convention) |
| `polymorphism.py` | Mixed list of `Resistor` and `Capacitor` objects; one `describe()` call works for all |
| `capacitor_class.py` | A `Capacitor` class with `charge()` computing `Q = C * V` |
| `read_only_property.py` | `Resistor` with a read-only `@property` for resistance |
| `validated_property.py` | `Resistor` with a `@property` plus a validated setter |

## Lecture material

| File | What it is |
|------|------------|
| `inheritance_lecture.md` | 45-minute lecture plan on Python inheritance |
| `python_classes_slides.pptx` | Slides for the classes lecture |
| `python_inheritance_slides.pptx` | Slides for the inheritance lecture |

## How to run

```bash
cd 04_object_oriented
python student_records.py
```

Note: `using_dog_class.py` imports `dog_class.py`, so run it from the
`04_object_oriented/` folder so the import resolves.

## Next steps

After mastering OOP, move on to **05_applications_electronics** to see how
these concepts apply to real-world electronics problems.
