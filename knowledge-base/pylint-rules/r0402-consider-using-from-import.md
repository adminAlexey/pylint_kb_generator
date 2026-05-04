---
id: pylint-R0402
rule_code: "R0402"
rule_name: "consider-using-from-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-from-import.html"
---
# consider-using-from-import / R0402

**Message emitted:**

`Use 'from %s import %s' instead`

**Description:**

*Emitted when a submodule of a package is imported and aliased with the same name, e.g., instead of ``import concurrent.futures as futures`` use ``from concurrent import futures``.*

**Problematic code:**

```
import os.path as path  # [consider-using-from-import]
```

**Correct code:**

```
from os import path
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.