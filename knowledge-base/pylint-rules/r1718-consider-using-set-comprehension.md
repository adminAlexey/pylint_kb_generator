---
id: pylint-R1718
rule_code: "R1718"
rule_name: "consider-using-set-comprehension"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-set-comprehension.html"
---
# consider-using-set-comprehension / R1718

**Message emitted:**

`Consider using a set comprehension`

**Description:**

*Although there is nothing syntactically wrong with this code, it is hard to read and can be simplified to a set comprehension. Also it is faster since you don't need to create another transient list*

**Problematic code:**

```
NUMBERS = [1, 2, 2, 3, 4, 4]

# +1: [consider-using-set-comprehension]
UNIQUE_EVEN_NUMBERS = set([number for number in NUMBERS if number % 2 == 0])
```

**Correct code:**

```
NUMBERS = [1, 2, 2, 3, 4, 4]

UNIQUE_EVEN_NUMBERS = {number for number in NUMBERS if number % 2 == 0}
```

**Additional details:**

[pyupgrade](https://github.com/asottile/pyupgrade) or [ruff](https://docs.astral.sh/ruff/) can fix this issue automatically.

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.