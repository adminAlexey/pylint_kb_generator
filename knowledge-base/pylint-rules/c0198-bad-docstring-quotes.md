---
id: pylint-C0198
rule_code: "C0198"
rule_name: "bad-docstring-quotes"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/bad-docstring-quotes.html"
---
# bad-docstring-quotes / C0198

**Message emitted:**

`Bad docstring quotes in %s, expected """, given %s`

**Description:**

*Used when a docstring does not have triple double quotes.*

**Problematic code:**

```
def foo():  # [bad-docstring-quotes]
    "Docstring."
    return
```

**Correct code:**

```
def foo():
    """Docstring."""
    return
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.docstyle
```

**Additional details:**

**FromPEP 257:**
: "For consistency, always use"""tripledoublequotes"""around docstrings."

**Related links:**

- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/#specification)

Note

This message is emitted by the optional ['docstyle'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-docstyle)
checker, which requires the `pylint.extensions.docstyle` plugin to be loaded.

Created by the [docstyle](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/docstyle.py) checker.