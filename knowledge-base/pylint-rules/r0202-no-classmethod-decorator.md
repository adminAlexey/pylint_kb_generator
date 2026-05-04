---
id: pylint-R0202
rule_code: "R0202"
rule_name: "no-classmethod-decorator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-classmethod-decorator.html"
---
# no-classmethod-decorator / R0202

**Message emitted:**

`Consider using a decorator instead of calling classmethod`

**Description:**

*Used when a class method is defined without using the decorator syntax.*

**Problematic code:**

```
class Fruit:
    COLORS = []

    def __init__(self, color):
        self.color = color

    def pick_colors(cls, *args):
        """classmethod to pick fruit colors"""
        cls.COLORS = args

    pick_colors = classmethod(pick_colors)  # [no-classmethod-decorator]
```

**Correct code:**

```
class Fruit:
    COLORS = []

    def __init__(self, color):
        self.color = color

    @classmethod
    def pick_colors(cls, *args):
        """classmethod to pick fruit colors"""
        cls.COLORS = args
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.