---
id: pylint-R1731
rule_code: "R1731"
rule_name: "consider-using-max-builtin"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-max-builtin.html"
---
# consider-using-max-builtin / R1731

**Message emitted:**

`Consider using '%s' instead of unnecessary if block`

**Description:**

*Using the max builtin instead of a conditional improves readability and conciseness.*

**Problematic code:**

```
def get_max(value1, value2):
    if value1 < value2:  # [consider-using-max-builtin]
        value1 = value2
    return value1

print(get_max(1, 2))
```

**Correct code:**

```
print(max(1, 2))
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.