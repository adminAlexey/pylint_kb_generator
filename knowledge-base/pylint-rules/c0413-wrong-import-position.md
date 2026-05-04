---
id: pylint-C0413
rule_code: "C0413"
rule_name: "wrong-import-position"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/wrong-import-position.html"
---
# wrong-import-position / C0413

**Message emitted:**

`Import "%s" should be placed at the top of the module`

**Description:**

*Used when code and imports are mixed.*

**Problematic code:**

```
import os

home = os.environ["HOME"]

import sys  # [wrong-import-position]

print(f"Home directory is {home}", file=sys.stderr)
```

**Correct code:**

```
import os
import sys

home = os.environ["HOME"]
print(f"Home directory is {home}", file=sys.stderr)
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.