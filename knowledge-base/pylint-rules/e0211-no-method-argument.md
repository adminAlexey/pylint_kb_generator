---
id: pylint-E0211
rule_code: "E0211"
rule_name: "no-method-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/no-method-argument.html"
---
# no-method-argument / E0211

**Message emitted:**

`Method %r has no argument`

**Description:**

*Used when a method which should have the bound instance as first argument has no argument defined.*

**Problematic code:**

```
class Person:
    def print_greeting():  # [no-method-argument]
        print("hello")
```

**Correct code:**

```
class Person:
    def print_greeting(self):
        print("hello")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.