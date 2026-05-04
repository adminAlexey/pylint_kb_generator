---
id: pylint-E1201
rule_code: "E1201"
rule_name: "logging-format-truncated"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/logging-format-truncated.html"
---
# logging-format-truncated / E1201

**Message emitted:**

`Logging format string ends in middle of conversion specifier`

**Description:**

*Used when a logging statement format string terminates before the end of a conversion specifier.*

**Problematic code:**

```
import logging
import sys

logging.warning("Python version: %", sys.version)  # [logging-format-truncated]
```

**Correct code:**

```
import logging
import sys

logging.warning("Python version: %s", sys.version)
```

Created by the [logging](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/logging.py) checker.