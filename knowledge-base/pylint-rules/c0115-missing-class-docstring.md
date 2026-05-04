---
id: pylint-C0115
rule_code: "C0115"
rule_name: "missing-class-docstring"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/missing-class-docstring.html"
---
# missing-class-docstring / C0115

**Message emitted:**

`Missing class docstring`

**Description:**

*Used when a class has no docstring. Even an empty class must have a docstring.*

**Problematic code:**

```
class Person:  # [missing-class-docstring]
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
```

**Correct code:**

```
class Person:
    """Class representing a person"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/docstring_checker.py) checker.