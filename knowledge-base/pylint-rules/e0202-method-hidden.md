---
id: pylint-E0202
rule_code: "E0202"
rule_name: "method-hidden"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/method-hidden.html"
---
# method-hidden / E0202

**Message emitted:**

`An attribute defined in %s line %s hides this method`

**Description:**

*Used when a class defines a method which is hidden by an instance attribute from an ancestor class or set by some client code.*

**Problematic code:**

```
class Fruit:
    def __init__(self, vitamins):
        self.vitamins = vitamins

    def vitamins(self):  # [method-hidden]
        pass
```

**Correct code:**

```
class Fruit:
    def __init__(self, vitamins):
        self.vitamins = vitamins

    def antioxidants(self):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.