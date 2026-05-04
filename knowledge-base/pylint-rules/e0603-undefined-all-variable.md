---
id: pylint-E0603
rule_code: "E0603"
rule_name: "undefined-all-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/undefined-all-variable.html"
---
# undefined-all-variable / E0603

**Message emitted:**

`Undefined variable name %r in __all__`

**Description:**

*Used when an undefined variable name is referenced in __all__.*

**Problematic code:**

```
__all__ = ["get_fruit_colour"]  # [undefined-all-variable]

def get_fruit_color():
    pass
```

**Correct code:**

```
__all__ = ["get_fruit_color"]

def get_fruit_color():
    pass
```

**Related links:**

- [Importing * From a Package](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.