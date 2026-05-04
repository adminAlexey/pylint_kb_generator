---
id: pylint-W1310
rule_code: "W1310"
rule_name: "format-string-without-interpolation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/format-string-without-interpolation.html"
---
# format-string-without-interpolation / W1310

**Message emitted:**

`Using formatting for a string that does not have any interpolated variables`

**Description:**

*Used when we detect a string that does not have any interpolation variables, in which case it can be either a normal string without formatting or a bug in the code.*

**Problematic code:**

```
print("number".format(1))  # [format-string-without-interpolation]
```

**Correct code:**

```
print("number: {}".format(1))
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.