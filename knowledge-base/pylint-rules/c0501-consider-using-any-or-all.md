---
id: pylint-C0501
rule_code: "C0501"
rule_name: "consider-using-any-or-all"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/consider-using-any-or-all.html"
---
# consider-using-any-or-all / C0501

**Message emitted:**

``for` loop could be `%s``

**Description:**

*A for loop that checks for a condition and return a bool can be replaced with any or all.*

**Problematic code:**

`all_even.py`:

```
def all_even(items):
    """Return True if the list contains all even numbers"""
    for item in items:  # [consider-using-any-or-all]
        if not item % 2 == 0:
            return False
    return True
```

`any_even.py`:

```
def any_even(items):
    """Return True if the list contains any even numbers"""
    for item in items:  # [consider-using-any-or-all]
        if item % 2 == 0:
            return True
    return False
```

**Correct code:**

`all_even.py`:

```
def all_even(items):
    """Return True if the list contains all even numbers"""
    return all(item % 2 == 0 for item in items)
```

`any_even.py`:

```
def any_even(items):
    """Return True if the list contains any even numbers"""
    return any(item % 2 == 0 for item in items)
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.for_any_all
```

Note

This message is emitted by the optional ['consider-using-any-or-all'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-for-any-all)
checker, which requires the `pylint.extensions.for_any_all` plugin to be loaded.

Created by the [consider-using-any-or-all](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/for_any_all.py) checker.