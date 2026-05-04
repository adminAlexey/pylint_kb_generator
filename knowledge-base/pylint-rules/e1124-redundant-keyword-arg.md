---
id: pylint-E1124
rule_code: "E1124"
rule_name: "redundant-keyword-arg"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/redundant-keyword-arg.html"
---
# redundant-keyword-arg / E1124

**Message emitted:**

`Argument %r passed by position and keyword in %s call`

**Description:**

*Used when a function call would result in assigning multiple values to a function parameter, one value from a positional argument and one from a keyword argument.*

**Problematic code:**

```
def square(x):
    return x * x

square(5, x=4)  # [redundant-keyword-arg]
```

**Correct code:**

`only_arg.py`:

```
def square(x):
    return x * x

square(5)
```

`only_kwarg.py`:

```
def square(x):
    return x * x

square(x=4)
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.