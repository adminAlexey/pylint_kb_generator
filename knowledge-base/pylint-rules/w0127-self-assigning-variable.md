---
id: pylint-W0127
rule_code: "W0127"
rule_name: "self-assigning-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/self-assigning-variable.html"
---
# self-assigning-variable / W0127

**Message emitted:**

`Assigning the same variable %r to itself`

**Description:**

*Emitted when we detect that a variable is assigned to itself*

**Problematic code:**

```
year = 2000
year = year  # [self-assigning-variable]
```

**Correct code:**

```
year = 2000
```

**Related links:**

- [Python assignment statement](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.