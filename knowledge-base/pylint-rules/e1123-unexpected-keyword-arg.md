---
id: pylint-E1123
rule_code: "E1123"
rule_name: "unexpected-keyword-arg"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unexpected-keyword-arg.html"
---
# unexpected-keyword-arg / E1123

**Message emitted:**

`Unexpected keyword argument %r in %s call`

**Description:**

*Used when a function call passes a keyword argument that doesn't correspond to one of the function's parameter names.*

**Problematic code:**

```
def print_coordinates(x=0, y=0):
    print(f"{x=}, {y=}")

print_coordinates(x=1, y=2, z=3)  # [unexpected-keyword-arg]
```

**Correct code:**

```
def print_coordinates(x=0, y=0):
    print(f"{x=}, {y=}")

print_coordinates(x=1, y=2)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.