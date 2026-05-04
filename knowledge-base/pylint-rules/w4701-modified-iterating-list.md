---
id: pylint-W4701
rule_code: "W4701"
rule_name: "modified-iterating-list"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/modified-iterating-list.html"
---
# modified-iterating-list / W4701

**Message emitted:**

`Iterated list '%s' is being modified inside for loop body, consider iterating through a copy of it instead.`

**Description:**

*Emitted when items are added or removed to a list being iterated through. Doing so can result in unexpected behaviour, that is why it is preferred to use a copy of the list.*

**Problematic code:**

```
fruits = ["apple", "orange", "mango"]
for fruit in fruits:
    fruits.append("pineapple")  # [modified-iterating-list]
```

**Correct code:**

```
fruits = ["apple", "orange", "mango"]
for fruit in fruits.copy():
    fruits.append("pineapple")
```

Created by the [modified_iteration](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/modified_iterating_checker.py) checker.