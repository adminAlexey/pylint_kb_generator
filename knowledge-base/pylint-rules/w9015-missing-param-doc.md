---
id: pylint-W9015
rule_code: "W9015"
rule_name: "missing-param-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-param-doc.html"
---
# missing-param-doc / W9015

**Message emitted:**

`"%s" missing in parameter documentation`

**Description:**

*Please add parameter declarations for all parameters.*

**Problematic code:**

```
def integer_sum(a: int, b):  # [missing-param-doc]
    """Returns sum of two integers
    :param a: first integer
    """
    return a + b
```

**Correct code:**

```
def integer_sum(a: int, b: int):
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    """
    return a + b
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