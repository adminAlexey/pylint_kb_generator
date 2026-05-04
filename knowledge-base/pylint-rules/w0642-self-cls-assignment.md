---
id: pylint-W0642
rule_code: "W0642"
rule_name: "self-cls-assignment"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/self-cls-assignment.html"
---
# self-cls-assignment / W0642

**Message emitted:**

`Invalid assignment to %s in method`

**Description:**

*Invalid assignment to self or cls in instance or class method respectively.*

**Problematic code:**

```
class Fruit:
    @classmethod
    def list_fruits(cls):
        cls = "apple"  # [self-cls-assignment]

    def print_color(self, *colors):
        self = "red"  # [self-cls-assignment]
        color = colors[1]
        print(color)
```

**Correct code:**

```
class Fruit:
    @classmethod
    def list_fruits(cls):
        fruit = "apple"
        print(fruit)

    def print_color(self, *colors):
        color = colors[1]
        print(color)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.