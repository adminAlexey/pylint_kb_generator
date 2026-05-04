---
id: pylint-C0112
rule_code: "C0112"
rule_name: "empty-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/empty-docstring.html"
---
# empty-docstring / C0112

**Message emitted:**

`Empty %s docstring`

**Description:**

*Used when a module, function, class or method has an empty docstring (it would be too easy ;).*

**Problematic code:**

```
def foo():  # [empty-docstring]
    """"""
```

**Correct code:**

```
def foo():
    """A dummy description."""
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/docstring_checker.py) checker.