---
id: pylint-W0137
rule_code: "W0137"
rule_name: "break-in-finally"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/break-in-finally.html"
---
# break-in-finally / W0137

**Message emitted:**

`'break' discouraged inside 'finally' clause`

**Description:**

*Emitted when the `break` keyword is found inside a finally clause. This will raise a SyntaxWarning starting in Python 3.14.*

**Problematic code:**

```
while True:
    try:
        pass
    finally:
        break  # [break-in-finally]
```

**Correct code:**

```
while True:
    try:
        pass
    except ValueError:
        pass
    else:
        break
```

**Related links:**

- [Python 3 docs 'finally' clause](https://docs.python.org/3/reference/compound_stmts.html#finally-clause)
- [PEP 765 - Disallow return/break/continue that exit a finally block](https://peps.python.org/pep-0765/)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.