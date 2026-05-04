---
id: pylint-W4905
rule_code: "W4905"
rule_name: "deprecated-decorator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-decorator.html"
---
# deprecated-decorator / W4905

**Message emitted:**

`Using deprecated decorator %s()`

**Description:**

*The decorator is marked as deprecated and will be removed in the future.*

**Problematic code:**

```
import abc

class Animal:
    @abc.abstractclassmethod  # [deprecated-decorator]
    def breath(cls):
        pass
```

**Correct code:**

```
import abc

class Animal:
    @abc.classmethod
    @abc.abstractmethod
    def breath(cls):
        pass
```

**Configuration file:**

```
[main]
py-version = 3.3
```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [stdlib](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/stdlib.py) checker.