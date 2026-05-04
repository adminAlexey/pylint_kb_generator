---
id: pylint-W0246
rule_code: "W0246"
rule_name: "useless-parent-delegation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/useless-parent-delegation.html"
---
# useless-parent-delegation / W0246

**Message emitted:**

`Useless parent or super() delegation in method %r`

**Description:**

*Used whenever we can detect that an overridden method is useless, relying on parent or super() delegation to do the same thing as another method from the MRO.*

**Problematic code:**

```
class Animal:
    def eat(self, food):
        print(f"Eating {food}")

class Human(Animal):
    def eat(self, food):  # [useless-parent-delegation]
        super(Human, self).eat(food)
```

**Correct code:**

```
class Animal:
    def eat(self, food):
        print(f"Eating {food}")

class Human(Animal):
    """There is no need to override 'eat' it has the same signature as the implementation in Animal."""
```

**Related links:**

- [Stackoverflow explanation for 'useless-super-delegation'](https://stackoverflow.com/a/51030674/2519059)

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.