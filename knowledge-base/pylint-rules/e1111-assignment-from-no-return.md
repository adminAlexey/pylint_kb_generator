---
id: pylint-E1111
rule_code: "E1111"
rule_name: "assignment-from-no-return"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/assignment-from-no-return.html"
---
# assignment-from-no-return / E1111

**Message emitted:**

`Assigning result of a function call, where the function has no return`

**Description:**

*Used when an assignment is done on a function call but the inferred function doesn't return anything.*

**Problematic code:**

```
def add(x, y):
    print(x + y)

value = add(10, 10)  # [assignment-from-no-return]
```

**Correct code:**

```
def add(x, y):
    return x + y

value = add(10, 10)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.