---
id: pylint-W0416
rule_code: "W0416"
rule_name: "shadowed-import"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/shadowed-import.html"
---
# shadowed-import / W0416

**Message emitted:**

`Shadowed %r (imported line %s)`

**Description:**

*Used when a module is aliased with a name that shadows another import.*

**Problematic code:**

```
from pathlib import Path

import FastAPI.Path as Path  # [shadowed-import]
```

**Correct code:**

```
from pathlib import Path

import FastAPI.Path as FastApiPath
```

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.