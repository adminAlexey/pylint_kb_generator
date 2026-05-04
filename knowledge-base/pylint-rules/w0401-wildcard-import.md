---
id: pylint-W0401
rule_code: "W0401"
rule_name: "wildcard-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/wildcard-import.html"
---
# wildcard-import / W0401

**Message emitted:**

`Wildcard import %s`

**Description:**

*Used when `from module import *` is detected.*

**Problematic code:**

```
from abc import *  # [wildcard-import]
```

**Correct code:**

```
# Either import module or
# only import required objects from module.
import abc
from abc import ABC, abstractmethod
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.