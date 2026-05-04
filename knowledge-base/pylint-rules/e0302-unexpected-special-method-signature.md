---
id: pylint-E0302
rule_code: "E0302"
rule_name: "unexpected-special-method-signature"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unexpected-special-method-signature.html"
---
# unexpected-special-method-signature / E0302

**Message emitted:**

`The special method %r expects %s param(s), %d %s given`

**Description:**

*Emitted when a special method was defined with an invalid number of parameters. If it has too few or too many, it might not work at all.*

**Problematic code:**

```
class ContextManager:
    def __enter__(self, context):  # [unexpected-special-method-signature]
        pass

    def __exit__(self, type):  # [unexpected-special-method-signature]
        pass
```

**Correct code:**

```
class ContextManager:
    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.