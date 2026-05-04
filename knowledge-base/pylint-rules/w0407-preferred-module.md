---
id: pylint-W0407
rule_code: "W0407"
rule_name: "preferred-module"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/preferred-module.html"
---
# preferred-module / W0407

**Message emitted:**

`Prefer importing %r instead of %r`

**Description:**

*Used when a module imported has a preferred replacement module.*

**Problematic code:**

```
import urllib  # [preferred-module]
```

**Correct code:**

```
import requests
```

**Configuration file:**

```
[IMPORTS]
preferred-modules=urllib:requests,
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.