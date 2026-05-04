---
id: pylint-E1305
rule_code: "E1305"
rule_name: "too-many-format-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/too-many-format-args.html"
---
# too-many-format-args / E1305

**Message emitted:**

`Too many arguments for format string`

**Description:**

*Used when a format string that uses unnamed conversion specifiers is given too many arguments.*

**Problematic code:**

```
# +1: [too-many-format-args]
print("Today is {0}, so tomorrow will be {1}".format("Monday", "Tuesday", "Wednesday"))
```

**Correct code:**

```
print("Today is {0}, so tomorrow will be {1}".format("Monday", "Tuesday"))
```

**Related links:**

- [String Formatting](https://docs.python.org/3/library/string.html#formatstrings)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.