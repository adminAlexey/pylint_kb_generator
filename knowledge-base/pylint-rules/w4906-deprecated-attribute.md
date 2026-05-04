---
id: pylint-W4906
rule_code: "W4906"
rule_name: "deprecated-attribute"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-attribute.html"
---
# deprecated-attribute / W4906

**Message emitted:**

`Using deprecated attribute %r`

**Description:**

*The attribute is marked as deprecated and will be removed in the future.*

**Problematic code:**

```
from configparser import ParsingError

err = ParsingError("filename")
source = err.filename  # [deprecated-attribute]
```

**Correct code:**

```
from configparser import ParsingError

err = ParsingError("filename")
source = err.source
```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.