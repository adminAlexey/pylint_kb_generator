---
id: pylint-R1723
rule_code: "R1723"
rule_name: "no-else-break"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-else-break.html"
---
# no-else-break / R1723

**Message emitted:**

`Unnecessary "%s" after "break", %s`

**Description:**

*Used in order to highlight an unnecessary block of code following an if containing a break statement. As such, it will warn when it encounters an else following a chain of ifs, all of them containing a break statement.*

**Problematic code:**

```
def next_seven_elements(iterator):
    for i, item in enumerate(iterator):
        if i == 7:  # [no-else-break]
            break
        else:
            yield item
```

**Correct code:**

```
def next_seven_elements(iterator):
    for i, item in enumerate(iterator):
        if i == 7:
            break
        yield item
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.