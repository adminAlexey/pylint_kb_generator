---
id: pylint-W0109
rule_code: "W0109"
rule_name: "duplicate-key"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/duplicate-key.html"
---
# duplicate-key / W0109

**Message emitted:**

`Duplicate key %r in dictionary`

**Description:**

*Used when a dictionary expression binds the same key multiple times.*

**Problematic code:**

```
test_score = {"Mathematics": 85, "Biology": 90, "Mathematics": 75}  # [duplicate-key]
```

**Correct code:**

```
test_score = {"Mathematics": 85, "Biology": 90, "History": 75}
```

**Related links:**

- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.