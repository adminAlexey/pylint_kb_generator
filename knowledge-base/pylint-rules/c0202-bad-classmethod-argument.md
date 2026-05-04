---
id: pylint-C0202
rule_code: "C0202"
rule_name: "bad-classmethod-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/bad-classmethod-argument.html"
---
# bad-classmethod-argument / C0202

**Message emitted:**

`Class method %s should have %s as first argument`

**Description:**

*Used when a class method has a first argument named differently than the value specified in valid-classmethod-first-arg option (default to "cls"), recommended to easily differentiate them from regular instance methods.*

**Problematic code:**

```
class Klass:
    @classmethod
    def get_instance(self):  # [bad-classmethod-argument]
        return self()
```

**Correct code:**

```
class Klass:
    @classmethod
    def get_instance(cls):
        return cls()
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.