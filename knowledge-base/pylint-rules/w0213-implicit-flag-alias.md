---
id: pylint-W0213
rule_code: "W0213"
rule_name: "implicit-flag-alias"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/implicit-flag-alias.html"
---
# implicit-flag-alias / W0213

**Message emitted:**

`Flag member %(overlap)s shares bit positions with %(sources)s`

**Description:**

*Used when multiple integer values declared within an enum.IntFlag class share a common bit position.*

**Problematic code:**

```
from enum import IntFlag

class FilePermissions(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 3  # [implicit-flag-alias]
```

**Correct code:**

```
from enum import IntFlag

class FilePermissions(IntFlag):
    READ = 1
    WRITE = 2
    EXECUTE = 4
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.