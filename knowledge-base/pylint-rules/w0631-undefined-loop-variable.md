---
id: pylint-W0631
rule_code: "W0631"
rule_name: "undefined-loop-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/undefined-loop-variable.html"
---
# undefined-loop-variable / W0631

**Message emitted:**

`Using possibly undefined loop variable %r`

**Description:**

*Used when a loop variable (i.e. defined by a for loop or a list comprehension or a generator expression) is used outside the loop.*

**Problematic code:**

```
def find_even_number(numbers):
    for x in numbers:
        if x % 2 == 0:
            break
    return x  # [undefined-loop-variable]
```

**Correct code:**

```
def find_even_number(numbers):
    for x in numbers:
        if x % 2:
            return x
    return None
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.