---
id: pylint-W9010
rule_code: "W9010"
rule_name: "redundant-yields-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redundant-yields-doc.html"
---
# redundant-yields-doc / W9010

**Message emitted:**

`Redundant yields documentation`

**Description:**

*Please remove the yields documentation from this method.*

**Problematic code:**

```
def give_fruits(fruits):  # [redundant-yields-doc]
    """Something about fruits

    Yields
    -------
        list
            fruits
    """
    return fruits
```

**Correct code:**

```
def give_fruits(fruits):
    """Something about fruits

    Yields
    -------
        str
            fruit
    """
    for fruit in fruits:
        yield fruit
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