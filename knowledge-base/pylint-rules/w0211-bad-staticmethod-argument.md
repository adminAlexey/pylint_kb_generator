---
id: pylint-W0211
rule_code: "W0211"
rule_name: "bad-staticmethod-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-staticmethod-argument.html"
---
# bad-staticmethod-argument / W0211

**Message emitted:**

`Static method with %r as first argument`

**Description:**

*Used when a static method has "self" or a value specified in valid-classmethod-first-arg option or valid-metaclass-classmethod-first-arg option as first argument.*

**Problematic code:**

```
class Wolf:
    @staticmethod
    def eat(self):  # [bad-staticmethod-argument]
        pass
```

**Correct code:**

```
class Wolf:
    @staticmethod
    def eat(sheep):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.