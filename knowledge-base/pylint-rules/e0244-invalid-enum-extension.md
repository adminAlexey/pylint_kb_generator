---
id: pylint-E0244
rule_code: "E0244"
rule_name: "invalid-enum-extension"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-enum-extension.html"
---
# invalid-enum-extension / E0244

**Message emitted:**

`Extending inherited Enum class "%s"`

**Description:**

*Used when a class tries to extend an inherited Enum class. Doing so will raise a TypeError at runtime.*

**Problematic code:**

```
from enum import Enum

class Color(Enum):
    ORANGE = 1
    CHERRY = 2

class Fruit(Color):  # [invalid-enum-extension]
    APPLE = 3
```

**Correct code:**

```
from enum import Enum

class Color(Enum):
    ORANGE = 1
    CHERRY = 2

class Fruit(Enum):
    ORANGE = 1
    CHERRY = 2
    APPLE = 3
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.