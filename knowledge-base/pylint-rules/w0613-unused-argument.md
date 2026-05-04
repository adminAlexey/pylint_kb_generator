---
id: pylint-W0613
rule_code: "W0613"
rule_name: "unused-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-argument.html"
---
# unused-argument / W0613

**Message emitted:**

`Unused argument %r`

**Description:**

*Used when a function or method argument is not used.*

**Problematic code:**

```
def print_point(x, y):  # [unused-argument]
    print(f"Point is located at {x},{x}")
```

**Correct code:**

```
def print_point(x, y):
    print(f"Point is located at {x},{y}")
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.