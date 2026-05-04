---
id: pylint-R1724
rule_code: "R1724"
rule_name: "no-else-continue"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/no-else-continue.html"
---
# no-else-continue / R1724

**Message emitted:**

`Unnecessary "%s" after "continue", %s`

**Description:**

*Used in order to highlight an unnecessary block of code following an if containing a continue statement. As such, it will warn when it encounters an else following a chain of ifs, all of them containing a continue statement.*

**Problematic code:**

```
def even_number_under(n: int):
    for i in range(n):
        if i % 2 == 1:  # [no-else-continue]
            continue
        else:
            yield i
```

**Correct code:**

```
def even_number_under(n: int):
    for i in range(n):
        if i % 2 == 1:
            continue
        yield i
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.