---
id: pylint-R1711
rule_code: "R1711"
rule_name: "useless-return"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/useless-return.html"
---
# useless-return / R1711

**Message emitted:**

`Useless return at end of function or method`

**Description:**

*Emitted when a single "return" or "return None" statement is found at the end of function or method definition. This statement can safely be removed because Python will implicitly return None*

**Problematic code:**

```
import sys

def print_python_version():  # [useless-return]
    print(sys.version)
    return None
```

**Correct code:**

```
import sys

def print_python_version():
    print(sys.version)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.