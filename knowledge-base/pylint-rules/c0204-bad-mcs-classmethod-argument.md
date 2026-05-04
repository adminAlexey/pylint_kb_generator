---
id: pylint-C0204
rule_code: "C0204"
rule_name: "bad-mcs-classmethod-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/bad-mcs-classmethod-argument.html"
---
# bad-mcs-classmethod-argument / C0204

**Message emitted:**

`Metaclass class method %s should have %s as first argument`

**Description:**

*Used when a metaclass class method has a first argument named differently than the value specified in valid-metaclass-classmethod-first-arg option (default to "mcs"), recommended to easily differentiate them from regular instance methods.*

**Problematic code:**

```
class Meta(type):
    @classmethod
    def foo(some):  # [bad-mcs-classmethod-argument]
        pass
```

**Correct code:**

```
class Meta(type):
    @classmethod
    def foo(mcs):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.