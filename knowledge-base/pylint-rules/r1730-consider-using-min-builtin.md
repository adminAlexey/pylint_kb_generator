---
id: pylint-R1730
rule_code: "R1730"
rule_name: "consider-using-min-builtin"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-min-builtin.html"
---
# consider-using-min-builtin / R1730

**Message emitted:**

`Consider using '%s' instead of unnecessary if block`

**Description:**

*Using the min builtin instead of a conditional improves readability and conciseness.*

**Problematic code:**

```
def get_min(value1, value2):
    if value1 > value2:  # [consider-using-min-builtin]
        value1 = value2
    return value1

print(get_min(1, 2))
```

**Correct code:**

```
print(min(1, 2))
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.