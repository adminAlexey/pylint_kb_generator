---
id: pylint-E0704
rule_code: "E0704"
rule_name: "misplaced-bare-raise"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/misplaced-bare-raise.html"
---
# misplaced-bare-raise / E0704

**Message emitted:**

`The raise statement is not inside an except clause`

**Description:**

*Used when a bare raise is not used inside an except clause. This generates an error, since there are no active exceptions to be reraised. An exception to this rule is represented by a bare raise inside a finally clause, which might work, as long as an exception is raised inside the try block, but it is nevertheless a code smell that must not be relied upon.*

**Problematic code:**

```
def validate_positive(x):
    if x <= 0:
        raise  # [misplaced-bare-raise]
```

**Correct code:**

```
def validate_positive(x):
    if x <= 0:
        raise ValueError(f"{x} is not positive")
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.