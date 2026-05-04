---
id: pylint-C0203
rule_code: "C0203"
rule_name: "bad-mcs-method-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/bad-mcs-method-argument.html"
---
# bad-mcs-method-argument / C0203

**Message emitted:**

`Metaclass method %s should have %s as first argument`

**Description:**

*Used when a metaclass method has a first argument named differently than the value specified in valid-classmethod-first-arg option (default to "cls"), recommended to easily differentiate them from regular instance methods.*

**Problematic code:**

```
class Meta(type):
    def func(some):  # [bad-mcs-method-argument]
        pass
```

**Correct code:**

```
class Meta(type):
    def func(cls):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.