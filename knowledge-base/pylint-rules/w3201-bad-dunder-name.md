---
id: pylint-W3201
rule_code: "W3201"
rule_name: "bad-dunder-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-dunder-name.html"
---
# bad-dunder-name / W3201

**Message emitted:**

`Bad or misspelled dunder method name %s.`

**Description:**

*Used when a dunder method is misspelled or defined with a name not within the predefined list of dunder names.*

**Problematic code:**

```
class Apples:
    def _init_(self):  # [bad-dunder-name]
        pass

    def __hello__(self):  # [bad-dunder-name]
        print("hello")
```

**Correct code:**

```
class Apples:
    def __init__(self):
        pass

    def hello(self):
        print("hello")
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.dunder
```

Note

This message is emitted by the optional ['dunder'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-dunder)
checker, which requires the `pylint.extensions.dunder` plugin to be loaded.

Created by the [dunder](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/dunder.py) checker.