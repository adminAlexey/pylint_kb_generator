---
id: pylint-W0134
rule_code: "W0134"
rule_name: "return-in-finally"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/return-in-finally.html"
---
# return-in-finally / W0134

**Message emitted:**

`'return' shadowed by the 'finally' clause.`

**Description:**

*Emitted when a 'return' statement is found in a 'finally' block. This will overwrite the return value of a function and should be avoided.*

**Problematic code:**

```
def second_favorite():
    fruits = ["kiwi", "pineapple"]
    try:
        return fruits[1]
    finally:
        # because of this `return` statement, this function will always return "kiwi"
        return fruits[0]  # [return-in-finally]
```

**Correct code:**

```
def second_favorite():
    fruits = ["kiwi", "pineapple"]
    try:
        return fruits[1]
    except KeyError:
        ...

    return fruits[0]
```

**Related links:**

- [Python 3 docs 'finally' clause](https://docs.python.org/3/reference/compound_stmts.html#finally-clause)
- [PEP 765 - Disallow return/break/continue that exit a finally block](https://peps.python.org/pep-0765/)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.