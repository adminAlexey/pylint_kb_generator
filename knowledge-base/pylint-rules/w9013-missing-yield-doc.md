---
id: pylint-W9013
rule_code: "W9013"
rule_name: "missing-yield-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-yield-doc.html"
---
# missing-yield-doc / W9013

**Message emitted:**

`Missing yield documentation`

**Description:**

*Please add documentation about what this generator yields.*

**Problematic code:**

```
def even_number_under(n: int):  # [missing-yield-doc]
    """Prints even numbers smaller than n.
    Args:
        n: Upper limit of even numbers.
    """
    for i in range(n):
        if i % 2 == 1:
            continue
        yield i
```

**Correct code:**

```
from typing import Iterator

def even_number_under(n: int) -> Iterator[int]:
    """Prints even numbers smaller than n.
    Args:
        n: Upper limit of even numbers.

    Yields:
        even numbers
    """
    for i in range(n):
        if i % 2 == 1:
            continue
        yield i
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.docparams

[Parameter_documentation]
accept-no-yields-doc=no
```

**Additional details:**

This message is raised only when parameter `accept-no-yields-doc` is set to `no`.

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.