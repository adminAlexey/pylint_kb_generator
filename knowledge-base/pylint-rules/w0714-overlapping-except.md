---
id: pylint-W0714
rule_code: "W0714"
rule_name: "overlapping-except"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/overlapping-except.html"
---
# overlapping-except / W0714

**Message emitted:**

`Overlapping exceptions (%s)`

**Description:**

*Used when exceptions in handler overlap or are identical*

**Problematic code:**

```
def divide_x_by_y(x: float, y: float):
    try:
        print(x / y)
    except (ArithmeticError, FloatingPointError) as e:  # [overlapping-except]
        print(f"There was an issue: {e}")
```

**Correct code:**

`less_generic_first.py`:

```
def divide_x_by_y(x: float, y: float):
    try:
        print(x / y)
    except FloatingPointError as e:
        print(f"There was a FloatingPointError: {e}")
    except ArithmeticError as e:
        # FloatingPointError  were already caught at this point
        print(f"There was an OverflowError or a ZeroDivisionError: {e}")
```

`only_generic.py`:

```
def divide_x_by_y(x: float, y: float):
    try:
        print(x / y)
    except ArithmeticError as e:
        print(
            f"There was an OverflowError, a ZeroDivisionError or a FloatingPointError: {e}"
        )
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.overlapping_exceptions,
```

**Related links:**

- [Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

Note

This message is emitted by the optional ['overlap-except'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-overlapping-exceptions)
checker, which requires the `pylint.extensions.overlapping_exceptions` plugin to be loaded.

Created by the [overlap-except](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/overlapping_exceptions.py) checker.