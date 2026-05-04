---
id: pylint-E0402
rule_code: "E0402"
rule_name: "relative-beyond-top-level"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/relative-beyond-top-level.html"
---
# relative-beyond-top-level / E0402

**Message emitted:**

`Attempted relative import beyond top-level package`

**Description:**

*Used when a relative import tries to access too many levels in the current package.*

**Problematic code:**

```
from ................antigravity import NGField  # [relative-beyond-top-level]
```

**Correct code:**

`absolute_import.py`:

```
from physic.antigravity import NGField
```

`fix_the_relative_import.py`:

```
# Right number of dots in the import: you needed 15 dots, not 16, duh.
# from ...............antigravity import NGField
```

**Additional details:**

Absolute imports were strongly preferred, historically. Relative imports allow you
to reorganize packages without changing any code, but these days refactoring tools and IDEs
allow you to do that at almost no cost anyway if the imports are explicit/absolute.
Therefore, absolute imports are often still preferred over relative ones.

**Related links:**

- [Absolute vs. explicit relative import of Python module](https://stackoverflow.com/a/16748366/2519059)
- [Withdraw anti-recommendation of relative imports from documentation](https://bugs.python.org/msg118031)

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.