# Python Inheritance: 45-Minute Lecture

**Prerequisites:** classes, objects, `__init__`, `self`, methods (last week)
**Goal:** By the end, students can build a subclass, override a method, call `super()`, and explain why inheritance beats copy-pasting a class.

---

## Timeline

| Time | Segment | Type |
|------|---------|------|
| 0:00 to 0:05 | Hook and recap | Talk |
| 0:05 to 0:16 | Basic inheritance and overriding | Live code |
| 0:16 to 0:22 | Exercise 1 | Students code |
| 0:22 to 0:30 | `super()` | Live code |
| 0:30 to 0:37 | Exercise 2 | Students code |
| 0:37 to 0:42 | Polymorphism | Live code |
| 0:42 to 0:45 | Recap, common mistakes, homework | Talk |

---

## 0:00 to 0:05: Hook and Recap

**Say this:** "Last week you built classes: `Student`, `Dog`, `BankAccount`. Today's problem: what happens when two classes are almost the same, but not quite?"

**Show this on the board.** Two circuit components, built the way you'd build them after last week:

```python
class Resistor:
    def __init__(self, name, resistance):
        self.name = name
        self.resistance = resistance

    def describe(self):
        return f"{self.name}: {self.resistance} ohms"


class Capacitor:
    def __init__(self, name, resistance, capacitance):
        self.name = name
        self.resistance = resistance
        self.capacitance = capacitance

    def describe(self):
        return f"{self.name}: {self.resistance} ohms, {self.capacitance} F"
```

**Ask:** "What's duplicated here?" Let them spot it: `name`, `resistance`, and most of `describe`, copied into a second class. Now imagine ten types of components. A change to how every component stores its name means editing ten classes.

**The idea:** Inheritance lets one class start from another. You write the shared part once, in a **parent** (or base) class, and each **child** (or subclass) adds only what makes it different.

**Analogy to use:** Every component on a breadboard shares things like a name and two leads. A resistor is a component that adds resistance. A capacitor is a component that adds capacitance. You don't redefine "has a name" for each one, you inherit it.

---

## 0:05 to 0:16: Basic Inheritance and Overriding

Live code this step by step.

### Step 1: A base class

```python
class Component:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name}: generic component"

c = Component("C1")
print(c.describe())
```

Nothing new here, this is last week's class.

### Step 2: A child class

```python
class Resistor(Component):
    pass

r = Resistor("R1")
print(r.name)
print(r.describe())
```

**Key points to say out loud:**

- `class Resistor(Component):` means "Resistor inherits from Component."
- `Resistor` has no `__init__` of its own, so Python uses `Component`'s.
- `r.name` and `r.describe()` work even though we never wrote them inside `Resistor`. They came from the parent.

### Step 3: Add what's different

```python
class Resistor(Component):
    def __init__(self, name, resistance):
        self.name = name
        self.resistance = resistance

    def describe(self):
        return f"{self.name}: {self.resistance} ohms"

r = Resistor("R1", 220)
print(r.describe())
```

Ask: "Is this better than copy-pasting `Capacitor` from scratch?" Not yet, since we rewrote `self.name = name` again. That's the problem `super()` solves, coming up in twenty minutes. For now, this is the shape: **override** `__init__` and `describe` when the child needs to store or report something the parent didn't.

### Step 4: `isinstance` and the family tree

```python
print(isinstance(r, Resistor))
print(isinstance(r, Component))
print(isinstance(c, Resistor))
```

**Point out:** every `Resistor` is a `Component`, but not every `Component` is a `Resistor`. Inheritance is one-directional.

**Check for understanding:** Ask "if `Capacitor` inherits from `Component`, and I call `isinstance(some_capacitor, Component)`, what prints?" (`True`.)

---

## 0:16 to 0:22: Exercise 1 (6 minutes)

**Task:** Build a `Vehicle` base class and a `Motorcycle` subclass.

1. `Vehicle.__init__` takes `make` and `top_speed`, stores both.
2. `Vehicle.describe()` returns `f"{self.make}, top speed {self.top_speed} km/h"`.
3. `Motorcycle` inherits from `Vehicle`. Give it its own `__init__` that also stores `has_sidecar` (a bool).
4. `Motorcycle.describe()` should return the same string as `Vehicle.describe()`, plus `", with sidecar"` if `has_sidecar` is `True`.

**Solution:**

```python
class Vehicle:
    def __init__(self, make, top_speed):
        self.make = make
        self.top_speed = top_speed

    def describe(self):
        return f"{self.make}, top speed {self.top_speed} km/h"


class Motorcycle(Vehicle):
    def __init__(self, make, top_speed, has_sidecar):
        self.make = make
        self.top_speed = top_speed
        self.has_sidecar = has_sidecar

    def describe(self):
        base = f"{self.make}, top speed {self.top_speed} km/h"
        if self.has_sidecar:
            base += ", with sidecar"
        return base


m = Motorcycle("Honda", 180, True)
print(m.describe())
```

**Walk the room.** Common errors here:

| Mistake | What you will see | Fix |
|---------|-------------------|-----|
| Forgetting `(Vehicle)` in the class line | `Motorcycle` has no relation to `Vehicle`, `isinstance` fails | `class Motorcycle(Vehicle):` |
| Calling `Motorcycle.describe(m)` instead of `m.describe()` | Works, but confuses class vs. object | Call through the object |
| Copying `describe` without adding the sidecar logic | Output missing the extra text | Reread the spec |

---

## 0:22 to 0:30: `super()`

**Transition:** "In the exercise, you rewrote `self.make = make` and `self.top_speed = top_speed` inside `Motorcycle`. That's still duplication. `super()` lets a child call its parent's method directly."

```python
class Component:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name}: generic component"


class Resistor(Component):
    def __init__(self, name, resistance):
        super().__init__(name)
        self.resistance = resistance

    def describe(self):
        base = super().describe()
        return base.replace("generic component", f"{self.resistance} ohms")

r = Resistor("R1", 220)
print(r.describe())
```

**Key points to say out loud:**

- `super().__init__(name)` calls `Component`'s `__init__`, which sets `self.name`. `Resistor` never repeats that line.
- `super().describe()` calls `Component`'s version of `describe`, and `Resistor` builds on top of the result instead of retyping it.
- `super()` always refers to the parent of the class you're currently writing.

### A cleaner version, without string surgery

```python
class Capacitor(Component):
    def __init__(self, name, capacitance):
        super().__init__(name)
        self.capacitance = capacitance

    def describe(self):
        return f"{super().describe()}, {self.capacitance} F capacitor"

cap = Capacitor("C1", 0.0001)
print(cap.describe())
```

**Say this:** "Notice `Capacitor` and `Resistor` both start their `describe()` by calling `super().describe()`. The shared part is written exactly once, in `Component`."

**Deliberate mistake to make live:** forget `super().__init__(name)` entirely.

```python
class Capacitor(Component):
    def __init__(self, name, capacitance):
        self.capacitance = capacitance

cap = Capacitor("C1", 0.0001)
print(cap.name)
```

This raises `AttributeError: 'Capacitor' object has no attribute 'name'`. Have students predict the error before you run it. Point out that `self.name` was never set, because `Component.__init__` never ran.

---

## 0:30 to 0:37: Exercise 2 (7 minutes)

**Task:** Rebuild `Motorcycle` from Exercise 1 using `super()`, then add a second subclass.

1. Rewrite `Motorcycle.__init__` to call `super().__init__(make, top_speed)` instead of setting `self.make` and `self.top_speed` directly.
2. Rewrite `Motorcycle.describe()` to call `super().describe()` and append the sidecar text.
3. Add a `Truck` class, also inheriting from `Vehicle`, that stores `cargo_capacity` (in kg) and overrides `describe()` to append `f", carries {self.cargo_capacity} kg"`.

**Solution:**

```python
class Vehicle:
    def __init__(self, make, top_speed):
        self.make = make
        self.top_speed = top_speed

    def describe(self):
        return f"{self.make}, top speed {self.top_speed} km/h"


class Motorcycle(Vehicle):
    def __init__(self, make, top_speed, has_sidecar):
        super().__init__(make, top_speed)
        self.has_sidecar = has_sidecar

    def describe(self):
        base = super().describe()
        if self.has_sidecar:
            base += ", with sidecar"
        return base


class Truck(Vehicle):
    def __init__(self, make, top_speed, cargo_capacity):
        super().__init__(make, top_speed)
        self.cargo_capacity = cargo_capacity

    def describe(self):
        return f"{super().describe()}, carries {self.cargo_capacity} kg"


m = Motorcycle("Honda", 180, True)
t = Truck("Volvo", 120, 9000)
print(m.describe())
print(t.describe())
```

**Stretch for fast finishers:** Add a `Vehicle.__str__` that calls `self.describe()`, so `print(m)` works without calling `.describe()` explicitly. This sets up the next section.

---

## 0:37 to 0:42: Polymorphism

**Transition:** "Real programs deal with many kinds of objects at once, without checking each one's exact type."

```python
components = [
    Resistor("R1", 220),
    Capacitor("C1", 0.0001),
    Resistor("R2", 1000),
]

for part in components:
    print(part.describe())
```

**Say this:** "The loop doesn't care whether `part` is a `Resistor` or a `Capacitor`. It just calls `describe()`, and each object answers in its own way. This is polymorphism: same method name, different behavior per class."

### Tie it back to the vehicles

```python
fleet = [
    Motorcycle("Honda", 180, True),
    Truck("Volvo", 120, 9000),
    Vehicle("Generic", 100),
]

for v in fleet:
    print(v.describe())
```

**Point out:** a plain `Vehicle` can sit in the same list as its subclasses, and `describe()` still works, since every subclass either inherits or overrides it.

**Check for understanding:** Ask "if I add a `Sedan(Vehicle)` class tomorrow with its own `describe()`, do I need to change this `for` loop?" (No. That's the payoff.)

---

## 0:42 to 0:45: Recap, Common Mistakes, Homework

### Recap (say these as a checklist)

1. `class Child(Parent):` makes `Child` inherit from `Parent`.
2. A child gets the parent's attributes and methods for free, unless it overrides them.
3. **Overriding** means writing a method in the child with the same name as one in the parent.
4. `super().__init__(...)` runs the parent's constructor, so shared setup is written once.
5. `super().method_name()` calls the parent's version of a method from inside an override.
6. **Polymorphism**: a loop can call the same method on different subclasses, and each behaves according to its own class.

### Mistakes to watch for this week

- Forgetting `(Parent)` in the class definition line.
- Overriding `__init__` and forgetting `super().__init__(...)`, leaving parent attributes unset.
- Calling `super.describe()` instead of `super().describe()` (missing parentheses after `super`).
- Rewriting the entire parent method in the child instead of calling `super()` and adding to it.

### Homework

**Part A (required):** Build a `Sensor` base class with `__init__(self, name, unit)` and `describe()` returning `f"{self.name} reads in {self.unit}"`. Build a `TemperatureSensor(Sensor)` that adds a `reading` value and overrides `describe()` to append the current reading, using `super()` for both.

**Part B (required):** Build an `Animal` base class with a `speak()` method returning `"..."`. Build `Dog` and `Cat` subclasses that override `speak()` to return `"Woof"` and `"Meow"`. Put three animals in a list and print what each one says using a single loop.

**Part C (challenge):** Extend the `Component` example with a `Diode` subclass that stores `forward_voltage`. Then write a function `total_description(parts)` that takes a list of any `Component` subclass and returns one string joining every `describe()` with a comma, without checking any object's type by hand.

---

## Instructor Notes

**If you are running ahead:** Cover `__str__` calling `self.describe()` from the stretch task, or briefly mention multiple levels of inheritance (a `Transistor` inheriting from a hypothetical `ActiveComponent`, which inherits from `Component`).

**If you are running behind:** Cut the `Truck` half of Exercise 2 and the fleet example in Polymorphism. Keep the `Resistor`/`Capacitor` polymorphism loop, since it's the clearest payoff of the whole lecture.

**If students are confused by `super()`:** Draw the two classes as stacked boxes, `Component` below `Resistor`. Circle `self.name = name` in the bottom box and draw an arrow from `super().__init__(name)` in the top box down to it. The point is that `super()` is just "go run this line in the parent."

**Live coding tip:** The missing `super().__init__()` mistake in the `super()` section is worth doing exactly as written. Students who see `AttributeError: no attribute 'name'` and figure out why tend to never make that mistake again.

**Next lecture teaser:** Encapsulation and property decorators, controlling how attributes are read and changed from outside a class.
