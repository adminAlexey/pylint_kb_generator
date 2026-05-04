---
id: pylint-W0125
rule_code: "W0125"
rule_name: "using-constant-test"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/using-constant-test.html"
---
# using-constant-test / W0125

**Message emitted:**

`Using a conditional statement with a constant value`

**Description:**

*Emitted when a conditional statement (If or ternary if) uses a constant value for its test. This might not be what the user intended to do.*

**Problematic code:**

```
if 0:  # [using-constant-test]
    print("This code is never executed.")
if 1:  # [using-constant-test]
    print("This code is always executed.")
```

**Correct code:**

```
print("This code is always executed.")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.