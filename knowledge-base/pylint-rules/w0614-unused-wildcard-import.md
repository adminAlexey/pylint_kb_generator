---
id: pylint-W0614
rule_code: "W0614"
rule_name: "unused-wildcard-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-wildcard-import.html"
---
# unused-wildcard-import / W0614

**Message emitted:**

`Unused import(s) %s from wildcard import of %s`

**Description:**

*Used when an imported module or variable is not used from a `'from X import *'` style import.*

**Problematic code:**

```
from abc import *  # [unused-wildcard-import]

class Animal(ABC): ...
```

**Correct code:**

```
from abc import ABC

class Animal(ABC): ...
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.