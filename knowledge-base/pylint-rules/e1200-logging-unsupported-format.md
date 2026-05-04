---
id: pylint-E1200
rule_code: "E1200"
rule_name: "logging-unsupported-format"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/logging-unsupported-format.html"
---
# logging-unsupported-format / E1200

**Message emitted:**

`Unsupported logging format character %r (%#02x) at index %d`

**Description:**

*Used when an unsupported format character is used in a logging statement format string.*

**Problematic code:**

```
import logging

logging.info("%s %y !", "Hello", "World")  # [logging-unsupported-format]
```

**Correct code:**

```
import logging

logging.info("%s %s !", "Hello", "World")
```

Created by the [logging](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/logging.py) checker.