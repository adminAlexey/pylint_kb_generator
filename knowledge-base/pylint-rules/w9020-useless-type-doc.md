---
id: pylint-W9020
rule_code: "W9020"
rule_name: "useless-type-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/useless-type-doc.html"
---
# useless-type-doc / W9020

**Message emitted:**

`"%s" useless ignored parameter type documentation`

**Description:**

*Please remove the ignored parameter type documentation.*

**Problematic code:**

```
def print_fruit(fruit, _):  # [useless-type-doc]
    """docstring ...

    Args:
        fruit (str): A fruit.
        _ (float): Another argument.
    """
    print(fruit)
```

**Correct code:**

```
def print_fruit(fruit):
    """docstring ...

    Args:
        fruit (str): A fruit.
    """
    print(fruit)
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.docparams,
```

Note

This message is emitted by the optional ['parameter_documentation'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docparams)
checker, which requires the `pylint.extensions.docparams` plugin to be loaded.

Created by the [parameter_documentation](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docparams.py) checker.