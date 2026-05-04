---
id: pylint-E0117
rule_code: "E0117"
rule_name: "nonlocal-without-binding"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/nonlocal-without-binding.html"
---
# nonlocal-without-binding / E0117

**Message emitted:**

`nonlocal name %s found without binding`

**Description:**

*Emitted when a nonlocal variable does not have an attached name somewhere in the parent scopes*

**Problematic code:**

```
class Fruit:
    def get_color(self):
        nonlocal colors  # [nonlocal-without-binding]
```

**Correct code:**

```
class Fruit:
    colors = ["red", "green"]

    def get_color(self):
        nonlocal colors
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.