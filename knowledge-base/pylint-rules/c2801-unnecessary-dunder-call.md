---
id: pylint-C2801
rule_code: "C2801"
rule_name: "unnecessary-dunder-call"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unnecessary-dunder-call.html"
---
# unnecessary-dunder-call / C2801

**Message emitted:**

`Unnecessarily calls dunder method %s. %s.`

**Description:**

*Used when a dunder method is manually called instead of using the corresponding function/method/operator.*

**Problematic code:**

```
three = (3.0).__str__()  # [unnecessary-dunder-call]
twelve = "1".__add__("2")  # [unnecessary-dunder-call]

def is_bigger_than_two(x):
    return x.__gt__(2)  # [unnecessary-dunder-call]
```

**Correct code:**

```
three = str(3.0)
twelve = "1" + "2"

def is_bigger_than_two(x):
    return x > 2
```

**Related links:**

- [Define dunder methods but don't call them directly](https://www.pythonmorsels.com/avoid-dunder-methods/)

Created by the [unnecessary-dunder-call](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/dunder_methods.py) checker.