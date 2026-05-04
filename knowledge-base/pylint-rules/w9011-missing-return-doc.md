---
id: pylint-W9011
rule_code: "W9011"
rule_name: "missing-return-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-return-doc.html"
---
# missing-return-doc / W9011

**Message emitted:**

`Missing return documentation`

**Description:**

*Please add documentation about what this method returns.*

**Problematic code:**

```
def integer_sum(a: int, b: int):  # [missing-return-doc]
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    """
    return a + b
```

**Correct code:**

```
def integer_sum(a: int, b: int) -> int:
    """Returns sum of two integers
    :param a: first integer
    :param b: second integer
    :return: sum of parameters a and b
    """
    return a + b
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.docparams

[Parameter_documentation]
accept-no-return-doc=no
```

**Additional details:**

This message is raised only when parameter `accept-no-return-doc` is set to `no`.

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.