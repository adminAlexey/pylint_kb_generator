---
id: pylint-W0611
rule_code: "W0611"
rule_name: "unused-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-import.html"
---
# unused-import / W0611

**Message emitted:**

`Unused %s`

**Description:**

*Used when an imported module or variable is not used.*

**Problematic code:**

```
from logging import getLogger
from pathlib import Path  # [unused-import]

LOGGER = getLogger(__name__)
```

**Correct code:**

```
from logging import getLogger

LOGGER = getLogger(__name__)
```

**Additional details:**

By default, this check is skipped for `__init__.py` files, as they often contain imports from submodules for the convenience of end users. While these imports are not used within `__init__.py`, they serve the purpose of providing intuitive import paths for the module's important classes and constants.

**Related links:**

- [--init-import](https://pylint.readthedocs.io/en/latest/configuration/all-options.html#variables-options)

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.