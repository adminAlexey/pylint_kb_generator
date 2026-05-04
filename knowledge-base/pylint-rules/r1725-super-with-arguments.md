---
id: pylint-R1725
rule_code: "R1725"
rule_name: "super-with-arguments"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/super-with-arguments.html"
---
# super-with-arguments / R1725

**Message emitted:**

`Consider using Python 3 style super() without arguments`

**Description:**

*Emitted when calling the super() builtin with the current class and instance. On Python 3 these arguments are the default and they can be omitted.*

**Problematic code:**

```
class Fruit:
    pass

class Orange(Fruit):
    def __init__(self):
        super(Orange, self).__init__()  # [super-with-arguments]
```

**Correct code:**

```
class Fruit:
    pass

class Orange(Fruit):
    def __init__(self):
        super().__init__()
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.