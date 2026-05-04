---
id: pylint-W9018
rule_code: "W9018"
rule_name: "differing-type-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/differing-type-doc.html"
---
# differing-type-doc / W9018

**Message emitted:**

`"%s" differing in parameter type documentation`

**Description:**

*Please check parameter names in type declarations.*

**Problematic code:**

```
def add(x: int, y: int):  # [differing-type-doc]
    """Add two numbers.

    :param int xy: x value.
    :param str y: y value.
    """

    return x + y
```

**Correct code:**

```
def add(x, y):
    """Add two numbers.

    :param int x: x value.
    :param int y: y value.
    """

    return x + y
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.docparams
```

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.