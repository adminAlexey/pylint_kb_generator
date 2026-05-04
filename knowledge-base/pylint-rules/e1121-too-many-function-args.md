---
id: pylint-E1121
rule_code: "E1121"
rule_name: "too-many-function-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/too-many-function-args.html"
---
# too-many-function-args / E1121

**Message emitted:**

`Too many positional arguments for %s call`

**Description:**

*Used when a function call passes too many positional arguments.*

**Problematic code:**

```
class Fruit:
    def __init__(self, color):
        self.color = color

apple = Fruit("red", "apple", [1, 2, 3])  # [too-many-function-args]
```

**Correct code:**

```
class Fruit:
    def __init__(self, color, name):
        self.color = color
        self.name = name

apple = Fruit("red", "apple")
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.