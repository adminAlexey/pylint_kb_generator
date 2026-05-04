---
id: pylint-W0604
rule_code: "W0604"
rule_name: "global-at-module-level"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/global-at-module-level.html"
---
# global-at-module-level / W0604

**Message emitted:**

`Using the global statement at the module level`

**Description:**

*Used when you use the "global" statement at the module level since it has no effect.*

**Problematic code:**

```
price = 25
global price  # [global-at-module-level]
```

**Correct code:**

```
price = 25
```

**Related links:**

- [Official Python FAQ - global and local](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)
- [PEP 3104 - Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)
- [Python global statement](https://docs.python.org/3/reference/simple_stmts.html#global)

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.