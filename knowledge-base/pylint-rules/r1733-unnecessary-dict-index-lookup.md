---
id: pylint-R1733
rule_code: "R1733"
rule_name: "unnecessary-dict-index-lookup"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/unnecessary-dict-index-lookup.html"
---
# unnecessary-dict-index-lookup / R1733

**Message emitted:**

`Unnecessary dictionary index lookup, use '%s' instead`

**Description:**

*Emitted when iterating over the dictionary items (key-item pairs) and accessing the value by index lookup. The value can be accessed directly instead.*

**Problematic code:**

```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}

for fruit_name, fruit_count in FRUITS.items():
    print(FRUITS[fruit_name])  # [unnecessary-dict-index-lookup]
```

**Correct code:**

```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}

for fruit_name, fruit_count in FRUITS.items():
    print(fruit_count)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.