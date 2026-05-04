---
id: pylint-E1519
rule_code: "E1519"
rule_name: "singledispatch-method"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/singledispatch-method.html"
---
# singledispatch-method / E1519

**Message emitted:**

`singledispatch decorator should not be used with methods, use singledispatchmethod instead.`

**Description:**

*singledispatch should decorate functions and not class/instance methods. Use singledispatchmethod for those cases.*

**Problematic code:**

```
from functools import singledispatch

class Board:
    @singledispatch  # [singledispatch-method]
    def convert_position(self, position):
        pass

    @convert_position.register  # [singledispatch-method]
    def _(self, position: str) -> tuple:
        position_a, position_b = position.split(",")
        return (int(position_a), int(position_b))

    @convert_position.register  # [singledispatch-method]
    def _(self, position: tuple) -> str:
        return f"{position[0]},{position[1]}"
```

**Correct code:**

```
from functools import singledispatch

@singledispatch
def convert_position(position):
    print(position)

@convert_position.register
def _(position: str) -> tuple:
    position_a, position_b = position.split(",")
    return (int(position_a), int(position_b))

@convert_position.register
def _(position: tuple) -> str:
    return f"{position[0]},{position[1]}"
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.