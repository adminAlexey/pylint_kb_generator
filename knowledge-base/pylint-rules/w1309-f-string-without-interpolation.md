---
id: pylint-W1309
rule_code: "W1309"
rule_name: "f-string-without-interpolation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/f-string-without-interpolation.html"
---
# f-string-without-interpolation / W1309

**Message emitted:**

`Using an f-string that does not have any interpolated variables`

**Description:**

*Used when we detect an f-string that does not use any interpolation variables, in which case it can be either a normal string or a bug in the code.*

**Problematic code:**

```
x = 1
y = 2
print(f"x + y = x + y")  # [f-string-without-interpolation]
```

**Correct code:**

```
x = 1
y = 2
print(f"{x} + {y} = {x + y}")
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.