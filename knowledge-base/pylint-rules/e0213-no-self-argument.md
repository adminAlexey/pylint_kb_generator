---
id: pylint-E0213
rule_code: "E0213"
rule_name: "no-self-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/no-self-argument.html"
---
# no-self-argument / E0213

**Message emitted:**

`Method %r should have "self" as first argument`

**Description:**

*Used when a method has an attribute different the "self" as first argument. This is considered as an error since this is a so common convention that you shouldn't break it!*

**Problematic code:**

```
class Fruit:
    def __init__(this, name):  # [no-self-argument]
        this.name = name
```

**Correct code:**

```
class Fruit:
    def __init__(self, name):
        self.name = name
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.