---
id: pylint-E0602
rule_code: "E0602"
rule_name: "undefined-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/undefined-variable.html"
---
# undefined-variable / E0602

**Message emitted:**

`Undefined variable %r`

**Description:**

*Used when an undefined variable is accessed.*

**Problematic code:**

```
print(number + 2)  # [undefined-variable]
```

**Correct code:**

```
number = 3
print(number + 2)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.