---
id: pylint-W1203
rule_code: "W1203"
rule_name: "logging-fstring-interpolation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/logging-fstring-interpolation.html"
---
# logging-fstring-interpolation / W1203

**Message emitted:**

`Use %s formatting in logging functions`

**Description:**

*Used when a logging statement has a call form of "logging.<logging method>(f"...")".Use another type of string formatting instead. You can use % formatting but leave interpolation to the logging function by passing the parameters as arguments. If logging-format-interpolation is disabled then you can use str.format. If logging-not-lazy is disabled then you can use % formatting as normal.*

**Problematic code:**

```
import logging
import sys

logging.error(f"Python version: {sys.version}")  # [logging-fstring-interpolation]
```

**Correct code:**

```
import logging
import sys

logging.error("Python version: %s", sys.version)
```

**Additional details:**

This message permits to allow f-string in logging and still be warned of
`logging-format-interpolation`.

**Related links:**

- [logging variable data](https://docs.python.org/3/howto/logging.html#logging-variable-data)
- [Rationale](https://stackoverflow.com/questions/34619790)

Created by the [logging](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/logging.py) checker.