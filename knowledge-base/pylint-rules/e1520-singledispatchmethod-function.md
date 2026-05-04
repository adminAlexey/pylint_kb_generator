---
id: pylint-E1520
rule_code: "E1520"
rule_name: "singledispatchmethod-function"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/singledispatchmethod-function.html"
---
# singledispatchmethod-function / E1520

**Message emitted:**

`singledispatchmethod decorator should not be used with functions, use singledispatch instead.`

**Description:**

*singledispatchmethod should decorate class/instance methods and not functions. Use singledispatch for those cases.*

**Problematic code:**

```
from functools import singledispatchmethod

@singledispatchmethod  # [singledispatchmethod-function]
def convert_position(position):
    print(position)

@convert_position.register  # [singledispatchmethod-function]
def _(position: str) -> tuple:
    position_a, position_b = position.split(",")
    return (int(position_a), int(position_b))

@convert_position.register  # [singledispatchmethod-function]
def _(position: tuple) -> str:
    return f"{position[0]},{position[1]}"
```

**Correct code:**

```
from functools import singledispatchmethod

class Board:
    @singledispatchmethod
    def convert_position(cls, position):
        pass

    @singledispatchmethod
    @classmethod
    def _(cls, position: str) -> tuple:
        position_a, position_b = position.split(",")
        return (int(position_a), int(position_b))

    @singledispatchmethod
    @classmethod
    def _(cls, position: tuple) -> str:
        return f"{position[0]},{position[1]}"
```

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.