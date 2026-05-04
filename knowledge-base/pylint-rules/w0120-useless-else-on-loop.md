---
id: pylint-W0120
rule_code: "W0120"
rule_name: "useless-else-on-loop"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/useless-else-on-loop.html"
---
# useless-else-on-loop / W0120

**Message emitted:**

`Else clause on loop without a break statement, remove the else and de-indent all the code inside it`

**Description:**

*Loops should only have an else clause if they can exit early with a break statement, otherwise the statements under else should be on the same scope as the loop itself.*

**Problematic code:**

```
def find_even_number(numbers):
    for x in numbers:
        if x % 2 == 0:
            return x
    else:  # [useless-else-on-loop]
        print("Did not find an even number")
```

**Correct code:**

```
def find_even_number(numbers):
    for x in numbers:
        if x % 2 == 0:
            return x
    print("Did not find an even number")
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.