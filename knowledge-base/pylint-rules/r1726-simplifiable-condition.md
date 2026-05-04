---
id: pylint-R1726
rule_code: "R1726"
rule_name: "simplifiable-condition"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/simplifiable-condition.html"
---
# simplifiable-condition / R1726

**Message emitted:**

`Boolean condition "%s" may be simplified to "%s"`

**Description:**

*Emitted when a boolean condition is able to be simplified.*

**Problematic code:**

```
def has_apples(apples) -> bool:
    return bool(apples or False)  # [simplifiable-condition]
```

**Correct code:**

```
def has_apples(apples) -> bool:
    return bool(apples)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.