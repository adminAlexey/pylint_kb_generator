---
id: pylint-W1113
rule_code: "W1113"
rule_name: "keyword-arg-before-vararg"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/keyword-arg-before-vararg.html"
---
# keyword-arg-before-vararg / W1113

**Message emitted:**

`Keyword argument before variable positional arguments list in the definition of %s function`

**Description:**

*When defining a keyword argument before variable positional arguments, one can end up in having multiple values passed for the aforementioned parameter in case the method is called with keyword arguments.*

**Problematic code:**

```
def func(x=None, *args):  # [keyword-arg-before-vararg]
    return [x, *args]
```

**Correct code:**

```
def func(*args, x=None):
    return [*args, x]
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.