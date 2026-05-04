---
id: pylint-E0401
rule_code: "E0401"
rule_name: "import-error"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/import-error.html"
---
# import-error / E0401

**Message emitted:**

`Unable to import %s`

**Description:**

*Used when pylint has been unable to import a module.*

**Problematic code:**

```
from patlib import Path  # [import-error]
```

**Correct code:**

```
from pathlib import Path
```

**Additional details:**

This can happen if you're importing a package that is not installed in your environment, or if you made a typo.

The solution is to install the package via pip/setup.py/wheel or fix the typo.

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.