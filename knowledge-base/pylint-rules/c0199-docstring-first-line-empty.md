---
id: pylint-C0199
rule_code: "C0199"
rule_name: "docstring-first-line-empty"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/docstring-first-line-empty.html"
---
# docstring-first-line-empty / C0199

**Message emitted:**

`First line empty in %s docstring`

**Description:**

*Used when a blank line is found at the beginning of a docstring.*

**Problematic code:**

```
def foo():  # [docstring-first-line-empty]
    """
    Lorem Ipsum is simply dummy text of the printing and typesetting
    industry.

    Lorem Ipsum has been the industry's standard dummy text ever since the
    1500s, when an unknown printer took a galley of type and scrambled it
    to make a type specimen book
    """
```

**Correct code:**

```
def foo():
    """Lorem Ipsum is simply dummy text of the printing and typesetting
    industry.

    Lorem Ipsum has been the industry's standard dummy text ever since the
    1500s, when an unknown printer took a galley of type and scrambled it
    to make a type specimen book
    """
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.docstyle
```

Note

This message is emitted by the optional ['docstyle'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docstyle)
checker, which requires the `pylint.extensions.docstyle` plugin to be loaded.

Created by the [docstyle](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docstyle.py) checker.