---
id: pylint-W9006
rule_code: "W9006"
rule_name: "missing-raises-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-raises-doc.html"
---
# missing-raises-doc / W9006

**Message emitted:**

`"%s" not documented as being raised`

**Description:**

*Please document exceptions for all raised exception types.*

**Problematic code:**

```
def integer_sum(a: int, b: int):  # [missing-raises-doc]
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Function supports only integer parameters.")
    return a + b
```

**Correct code:**

```
def integer_sum(a: int, b: int):
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    :raises ValueError: One of the parameters is not an integer.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Function supports only integer parameters.")
    return a + b
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.docparams

[BASIC]
accept-no-raise-doc = no
```

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.