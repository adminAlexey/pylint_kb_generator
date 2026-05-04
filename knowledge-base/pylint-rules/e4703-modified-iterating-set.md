---
id: pylint-E4703
rule_code: "E4703"
rule_name: "modified-iterating-set"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/modified-iterating-set.html"
---
# modified-iterating-set / E4703

**Message emitted:**

`Iterated set '%s' is being modified inside for loop body, iterate through a copy of it instead.`

**Description:**

*Emitted when items are added or removed to a set being iterated through. Doing so raises a RuntimeError.*

**Problematic code:**

```
fruits = {"apple", "orange", "mango"}
for fruit in fruits:
    fruits.add(fruit + "yum")  # [modified-iterating-set]
```

**Correct code:**

```
fruits = {"apple", "orange", "mango"}
for fruit in fruits.copy():
    fruits.add(fruit + "yum")
```

Created by the [modified_iteration](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/modified_iterating_checker.py) checker.