---
id: pylint-W9019
rule_code: "W9019"
rule_name: "useless-param-doc"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/useless-param-doc.html"
---
# useless-param-doc / W9019

**Message emitted:**

`"%s" useless ignored parameter documentation`

**Description:**

*Please remove the ignored parameter documentation.*

**Problematic code:**

```
def say_hello(_new: str) -> str:  # [useless-param-doc]
    """say hello!

    :param _new:
    :return: comment
    """
    return "hello"
```

**Correct code:**

```
def say_hello(_new: str) -> str:
    """say hello!

    :return: comment
    """
    return "hello"
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