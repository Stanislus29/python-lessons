# Encapsulation — `@property`

Regent University College, Accra, Ghana

This topic supplements both the regular and weekend sessions. It covers
controlling how object attributes are read and changed from outside a class.

## Files

| File | What it does |
|------|--------------|
| `read_only_property.py` | `Resistor` with a read-only `@property` for resistance |
| `validated_property.py` | `Resistor` with a `@property` plus a validated setter (rejects non-positive values) |

## How to run

```bash
cd encapsulation
python read_only_property.py
python validated_property.py
```

## Teaching points

* `_name` (leading underscore) is a Python convention meaning "internal —
  treat with care". Python does not enforce true privacy.
* `@property` exposes an attribute for reading.
* `@<name>.setter` lets you control writes and add validation.
* Always validate data before storing it in an object.
