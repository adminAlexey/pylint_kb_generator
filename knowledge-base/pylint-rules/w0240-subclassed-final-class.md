---
id: pylint-W0240
rule_code: "W0240"
rule_name: "subclassed-final-class"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/subclassed-final-class.html"
---
# subclassed-final-class / W0240

**Message emitted:**

`Class %r is a subclass of a class decorated with typing.final: %r`

**Description:**

*Used when a class decorated with typing.final has been subclassed.*

**Problematic code:**

```
from typing import final

@final
class PlatypusData:
    """General Platypus data."""

    average_length = 46
    average_body_temperature = 32

class FluorescentPlaytipus(PlatypusData):  # [subclassed-final-class]
    """Playtipus with fluorescent fur."""
```

**Correct code:**

```
from typing import final

@final
class PlatypusData:
    """General Platypus data."""

    average_length = 46
    average_body_temperature = 32

def print_average_length_platypus():
    output = f"The average length of a platypus is: {PlatypusData.average_length}cm"
    print(output)
```

**Configuration file:**

```
[MAIN]
py-version=3.8
```

**Additional details:**

This message is emitted when a class which is decorated with final is subclassed; the decorator indicates that the class is not intended to be extended.

Note this message can't be emitted when using Python < 3.8.

**Related links:**

- [PEP 591](https://peps.python.org/pep-0591/#the-final-decorator)

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.