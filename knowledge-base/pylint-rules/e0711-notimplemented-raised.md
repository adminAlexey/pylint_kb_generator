---
id: pylint-E0711
rule_code: "E0711"
rule_name: "notimplemented-raised"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/notimplemented-raised.html"
---
# notimplemented-raised / E0711

**Message emitted:**

`NotImplemented raised - should raise NotImplementedError`

**Description:**

*Used when NotImplemented is raised instead of NotImplementedError*

**Problematic code:**

```
class Worm:
    def bore(self):
        raise NotImplemented  # [notimplemented-raised]
```

**Correct code:**

```
class Worm:
    def bore(self):
        raise NotImplementedError
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.