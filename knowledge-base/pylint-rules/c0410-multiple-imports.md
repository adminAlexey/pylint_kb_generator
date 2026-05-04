---
id: pylint-C0410
rule_code: "C0410"
rule_name: "multiple-imports"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/multiple-imports.html"
---
# multiple-imports / C0410

**Message emitted:**

`Multiple imports on one line (%s)`

**Description:**

*Used when import statement importing multiple modules is detected.*

**Problematic code:**

```
import os, sys  # [multiple-imports]
```

**Correct code:**

```
import os
import sys
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.