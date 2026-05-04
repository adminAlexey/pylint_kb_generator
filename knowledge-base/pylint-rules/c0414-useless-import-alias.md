---
id: pylint-C0414
rule_code: "C0414"
rule_name: "useless-import-alias"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/useless-import-alias.html"
---
# useless-import-alias / C0414

**Message emitted:**

`Import alias does not rename original package`

**Description:**

*Used when an import alias is same as original package, e.g., using import numpy as numpy instead of import numpy as np.*

**Problematic code:**

```
import pandas as pandas  # [useless-import-alias]
```

**Correct code:**

```
import pandas as pd
```

**Additional details:**

## Known issue

If you prefer to use "from-as" to explicitly reexport in API (`from fruit import orange as orange`)
instead of using `__all__` this message will be a false positive.

Use `--allow-reexport-from-package` to allow explicit reexports by alias
in package `__init__` files.

**Related links:**

- [--allow-reexport-from-package](https://pylint.readthedocs.io/en/latest/configuration/all-options.html#imports-options)
- [PEP 8, Import Guideline](https://peps.python.org/pep-0008/#imports)
- [Pylint block-disable](https://pylint.readthedocs.io/en/latest/user_guide/message_control.html#block-disables)
- [mypy --no-implicit-reexport](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-no-implicit-reexport)

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.