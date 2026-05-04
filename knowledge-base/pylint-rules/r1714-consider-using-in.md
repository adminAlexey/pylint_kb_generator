---
id: pylint-R1714
rule_code: "R1714"
rule_name: "consider-using-in"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-in.html"
---
# consider-using-in / R1714

**Message emitted:**

`Consider merging these comparisons with 'in' by using '%s %sin (%s)'. Use a set instead if elements are hashable.`

**Description:**

*To check if a variable is equal to one of many values, combine the values into a set or tuple and check if the variable is contained "in" it instead of checking for equality against each of the values. This is faster and less verbose.*

**Problematic code:**

```
def fruit_is_round(fruit):
    # +1: [consider-using-in]
    return fruit == "apple" or fruit == "orange" or fruit == "melon"
```

**Correct code:**

```
def fruit_is_round(fruit):
    return fruit in {"apple", "orange", "melon"}
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.