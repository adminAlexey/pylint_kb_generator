---
id: pylint-W9005
rule_code: "W9005"
rule_name: "multiple-constructor-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/multiple-constructor-doc.html"
---
# multiple-constructor-doc / W9005

**Message emitted:**

`"%s" has constructor parameters documented in class and __init__`

**Description:**

*Please remove parameter declarations in the class or constructor.*

**Problematic code:**

```
class Point:  # [multiple-constructor-doc]
    """Represents a point in the xy-coordinate plane.

    :param x: coordinate
    :param y: coordinate
    """

    def __init__(self, x, y):
        """Represents a point in the xy-coordinate plane.

        :param x: coordinate
        :param y: coordinate
        """
        self.x = x
        self.y = y
```

**Correct code:**

```
class Point:
    def __init__(self, x, y):
        """Represents a point in the xy-coordinate plane.

        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.docparams

[Parameter_documentation]
no-docstring-rgx=^(?!__init__$)_
```

**Additional details:**

Both docstrings are acceptable but not both at the same time.

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.