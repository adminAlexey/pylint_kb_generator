---
id: pylint-R0912
rule_code: "R0912"
rule_name: "too-many-branches"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/too-many-branches.html"
---
# too-many-branches / R0912

**Message emitted:**

`Too many branches (%s/%s)`

**Description:**

*Used when a function or method has too many branches, making it hard to follow.*

**Problematic code:**

```
def num_to_word(x):  # [too-many-branches]
    if x == 0:
        return "zero"
    elif x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    elif x == 4:
        return "four"
    elif x == 5:
        return "five"
    elif x == 6:
        return "six"
    elif x == 7:
        return "seven"
    elif x == 8:
        return "eight"
    elif x == 9:
        return "nine"
    else:
        return None
```

**Correct code:**

```
def num_to_word(x):
    return {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }.get(x)
```

**Configuration file:**

```
[main]
max-branches=10
```

Created by the [design](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/design_analysis.py) checker.