---
id: pylint-E3102
rule_code: "E3102"
rule_name: "positional-only-arguments-expected"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/positional-only-arguments-expected.html"
---
# positional-only-arguments-expected / E3102

**Message emitted:**

``%s()` got some positional-only arguments passed as keyword arguments: %s`

**Description:**

*Emitted when positional-only arguments have been passed as keyword arguments. Remove the keywords for the affected arguments in the function call.*

**Problematic code:**

```
def cube(n, /):
    """Takes in a number n, returns the cube of n"""
    return n**3

cube(n=2)  # [positional-only-arguments-expected]
```

**Correct code:**

```
def cube(n, /):
    """Takes in a number n, returns the cube of n"""
    return n**3

cube(2)
```

**Related links:**

- [PEP 570](https://peps.python.org/pep-570/)

Created by the [method_args](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/method_args.py) checker.