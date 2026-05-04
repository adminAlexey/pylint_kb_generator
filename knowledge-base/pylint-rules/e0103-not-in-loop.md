---
id: pylint-E0103
rule_code: "E0103"
rule_name: "not-in-loop"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/not-in-loop.html"
---
# not-in-loop / E0103

**Message emitted:**

`%r not properly in loop`

**Description:**

*Used when break or continue keywords are used outside a loop.*

**Problematic code:**

```
def print_even_numbers():
    for i in range(100):
        if i % 2 == 0:
            print(i)
    else:
        continue  # [not-in-loop]
```

**Correct code:**

```
def print_even_numbers():
    for i in range(100):
        if i % 2:
            continue
        print(i)
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.