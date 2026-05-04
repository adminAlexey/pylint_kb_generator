---
id: pylint-E0611
rule_code: "E0611"
rule_name: "no-name-in-module"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/no-name-in-module.html"
---
# no-name-in-module / E0611

**Message emitted:**

`No name %r in module %r`

**Description:**

*Used when a name cannot be found in a module.*

**Problematic code:**

```
from os import pizza  # [no-name-in-module]
```

**Correct code:**

```
from os import path
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.