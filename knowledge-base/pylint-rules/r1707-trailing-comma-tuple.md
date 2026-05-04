---
id: pylint-R1707
rule_code: "R1707"
rule_name: "trailing-comma-tuple"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/trailing-comma-tuple.html"
---
# trailing-comma-tuple / R1707

**Message emitted:**

`Disallow trailing comma tuple`

**Description:**

*In Python, a tuple is actually created by the comma symbol, not by the parentheses. Unfortunately, one can actually create a tuple by misplacing a trailing comma, which can lead to potential weird bugs in your code. You should always use parentheses explicitly for creating a tuple.*

**Problematic code:**

```
COMPASS = "north", "south", "east", "west",  # [trailing-comma-tuple]
```

**Correct code:**

```
COMPASS = ("north", "south", "east", "west")
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.