---
id: pylint-W0632
rule_code: "W0632"
rule_name: "unbalanced-tuple-unpacking"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unbalanced-tuple-unpacking.html"
---
# unbalanced-tuple-unpacking / W0632

**Message emitted:**

`Possible unbalanced tuple unpacking with sequence %s: left side has %d label%s, right side has %d value%s`

**Description:**

*Used when there is an unbalanced tuple unpacking in assignment*

**Problematic code:**

```
fruits = ("orange", "apple", "strawberry", "peer")
orange, apple, strawberry = fruits  # [unbalanced-tuple-unpacking]
```

**Correct code:**

```
fruits = ("orange", "apple", "strawberry", "peer")
orange, apple, *remaining_fruits = fruits
```

**Related links:**

- [PEP 3132 - Extended Iterable Unpacking](https://peps.python.org/pep-3132/)

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.