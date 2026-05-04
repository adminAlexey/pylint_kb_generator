---
id: pylint-R0203
rule_code: "R0203"
rule_name: "no-staticmethod-decorator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-staticmethod-decorator.html"
---
# no-staticmethod-decorator / R0203

**Message emitted:**

`Consider using a decorator instead of calling staticmethod`

**Description:**

*Used when a static method is defined without using the decorator syntax.*

**Problematic code:**

```
class Worm:
    def bore(self):
        pass

    bore = staticmethod(bore)  # [no-staticmethod-decorator]
```

**Correct code:**

```
class Worm:
    @staticmethod
    def bore(self):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.