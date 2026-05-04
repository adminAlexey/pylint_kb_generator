---
id: pylint-R1702
rule_code: "R1702"
rule_name: "too-many-nested-blocks"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/too-many-nested-blocks.html"
---
# too-many-nested-blocks / R1702

**Message emitted:**

`Too many nested blocks (%s/%s)`

**Description:**

*Used when a function or a method has too many nested blocks. This makes the code less understandable and maintainable.*

**Problematic code:**

```
def correct_fruits(fruits):
    if len(fruits) > 1:  # [too-many-nested-blocks]
        if "apple" in fruits:
            if "orange" in fruits:
                count = fruits["orange"]
                if count % 2:
                    if "kiwi" in fruits:
                        if count == 2:
                            return True
    return False
```

**Correct code:**

```
def correct_fruits(fruits):
    if len(fruits) > 1 and "apple" in fruits and "orange" in fruits:
        count = fruits["orange"]
        if count % 2 and "kiwi" in fruits and count == 2:
            return True
    return False
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.