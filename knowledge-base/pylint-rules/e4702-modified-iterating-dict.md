---
id: pylint-E4702
rule_code: "E4702"
rule_name: "modified-iterating-dict"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/modified-iterating-dict.html"
---
# modified-iterating-dict / E4702

**Message emitted:**

`Iterated dict '%s' is being modified inside for loop body, iterate through a copy of it instead.`

**Description:**

*Emitted when items are added or removed to a dict being iterated through. Doing so raises a RuntimeError.*

**Problematic code:**

```
fruits = {"apple": 1, "orange": 2, "mango": 3}

i = 0
for fruit in fruits:
    fruits["apple"] = i  # [modified-iterating-dict]
    i += 1
```

**Correct code:**

```
fruits = {"apple": 1, "orange": 2, "mango": 3}

i = 0
for fruit in fruits.copy():
    fruits["apple"] = i
    i += 1
```

Created by the [modified_iteration](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/modified_iterating_checker.py) checker.