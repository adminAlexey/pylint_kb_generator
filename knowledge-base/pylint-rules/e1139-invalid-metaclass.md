---
id: pylint-E1139
rule_code: "E1139"
rule_name: "invalid-metaclass"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-metaclass.html"
---
# invalid-metaclass / E1139

**Message emitted:**

`Invalid metaclass %r used`

**Description:**

*Emitted whenever we can detect that a class is using, as a metaclass, something which might be invalid for using as a metaclass.*

**Problematic code:**

```
class Apple(metaclass=int):  # [invalid-metaclass]
    pass
```

**Correct code:**

```
class Plant:
    pass

class Apple(Plant):
    pass
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.