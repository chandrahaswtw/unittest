# UNITTEST MODULE

`unittest` is an inbuilt testing module. The entire documentation is [here](https://docs.python.org/3/library/unittest.html).

## Naming rules

- We can have a `tests.py` file where we can specify the tests.
- Or we can have a folder `tests` and place all tests inside it.
    - This folder can be at any nested level.
    - The individual test case files must start with prefix `test_`. Else the file will be ignored.
- The class we use in the tests can be of any name, for naming convention we generally start with `Test` prefix.
- The methods inside class must start with `test_` else, it will be ignored.

## Executing tests

### Executing all tests

`python3 -m unittest`

### Executing single test file

`python3 -m unittest tests.test_calc`

## NOTES

### Assert functions

| Method | Checks That | New in |
|----------|-------------|---------|
| `assertEqual(a, b)` | `a == b` | - |
| `assertNotEqual(a, b)` | `a != b` | - |
| `assertTrue(x)` | `bool(x) is True` | - |
| `assertFalse(x)` | `bool(x) is False` | - |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |
| `assertIsSubclass(a, b)` | `issubclass(a, b)` | 3.14 |
| `assertNotIsSubclass(a, b)` | `not issubclass(a, b)` | 3.14 |
