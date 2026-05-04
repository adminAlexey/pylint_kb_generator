---
id: pylint-R1717
rule_code: "R1717"
rule_name: "consider-using-dict-comprehension"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-dict-comprehension.html"
---
# consider-using-dict-comprehension / R1717

**Message emitted:**

`Consider using a dictionary comprehension`

**Description:**

*Emitted when we detect the creation of a dictionary using the dict() callable and a transient list. Although there is nothing syntactically wrong with this code, it is hard to read and can be simplified to a dict comprehension. Also it is faster since you don't need to create another transient list*

**Problematic code:**

```
NUMBERS = [1, 2, 3]

# +1: [consider-using-dict-comprehension]
DOUBLED_NUMBERS = dict([(number, number * 2) for number in NUMBERS])
```

**Correct code:**

```
NUMBERS = [1, 2, 3]

DOUBLED_NUMBERS = {number: number * 2 for number in NUMBERS}
```

**Additional details:**

[pyupgrade](https://github.com/asottile/pyupgrade) or [ruff](https://docs.astral.sh/ruff/) can fix this issue automatically.

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.