---
id: pylint-E1901
rule_code: "E1901"
rule_name: "bare-name-capture-pattern"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bare-name-capture-pattern.html"
---
# bare-name-capture-pattern / E1901

**Message emitted:**

`The name capture `case %s` makes the remaining patterns unreachable. Use a dotted name (for example an enum) to fix this.`

**Description:**

*Emitted when a name capture pattern is used in a match statement and there are case statements below it.*

**Problematic code:**

```
red = 0
green = 1
blue = 2

def func(color):
    match color:
        case red:  # [bare-name-capture-pattern]
            print("I see red!")
        case green:  # [bare-name-capture-pattern]
            print("Grass is green")
        case blue:
            print("I'm feeling the blues :(")
```

**Correct code:**

```
from enum import Enum

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

def func(color: Color) -> None:
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
```

**Related links:**

- [PEP 636](https://peps.python.org/pep-0636/#matching-against-constants-and-enums)

Created by the [match_statements](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/match_statements_checker.py) checker.