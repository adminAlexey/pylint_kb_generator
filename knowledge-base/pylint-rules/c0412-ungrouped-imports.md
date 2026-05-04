---
id: pylint-C0412
rule_code: "C0412"
rule_name: "ungrouped-imports"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/ungrouped-imports.html"
---
# ungrouped-imports / C0412

**Message emitted:**

`Imports from package %s are not grouped`

**Description:**

*Used when imports are not grouped by packages.*

**Problematic code:**

```
import logging
import os
import sys
import logging.config  # [ungrouped-imports]
from logging.handlers import WatchedFileHandler
```

**Correct code:**

```
import logging
import logging.config
import os
import sys
from logging.handlers import FileHandler
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.