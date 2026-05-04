---
id: pylint-W1115
rule_code: "W1115"
rule_name: "non-str-assignment-to-dunder-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/non-str-assignment-to-dunder-name.html"
---
# non-str-assignment-to-dunder-name / W1115

**Message emitted:**

`Non-string value assigned to __name__`

**Description:**

*Emitted when a non-string value is assigned to __name__*

**Problematic code:**

```
class Fruit:
    pass

Fruit.__name__ = 1  # [non-str-assignment-to-dunder-name]
```

**Correct code:**

```
class Fruit:
    pass

Fruit.__name__ = "FRUIT"
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.