---
id: pylint-W9008
rule_code: "W9008"
rule_name: "redundant-returns-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/redundant-returns-doc.html"
---
# redundant-returns-doc / W9008

**Message emitted:**

`Redundant returns documentation`

**Description:**

*Please remove the return/rtype documentation from this method.*

**Problematic code:**

```
def print_fruits(fruits):  # [redundant-returns-doc]
    """Print list of fruits

    Returns
    -------
        str
    """
    print(fruits)
    return None
```

**Correct code:**

```
def print_fruits(fruits):
    """Print list of fruits

    Returns
    -------
        str
    """
    print(fruits)
    return ",".join(fruits)
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