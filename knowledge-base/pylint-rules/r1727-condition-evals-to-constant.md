---
id: pylint-R1727
rule_code: "R1727"
rule_name: "condition-evals-to-constant"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/condition-evals-to-constant.html"
---
# condition-evals-to-constant / R1727

**Message emitted:**

`Boolean condition '%s' will always evaluate to '%s'`

**Description:**

*Emitted when a boolean condition can be simplified to a constant value.*

**Problematic code:**

```
def is_a_fruit(fruit):
    return bool(fruit in {"apple", "orange"} or True)  # [condition-evals-to-constant]
```

**Correct code:**

```
def is_a_fruit(fruit):
    return fruit in {"apple", "orange"}
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.