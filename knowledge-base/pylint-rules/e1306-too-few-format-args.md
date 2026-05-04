---
id: pylint-E1306
rule_code: "E1306"
rule_name: "too-few-format-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/too-few-format-args.html"
---
# too-few-format-args / E1306

**Message emitted:**

`Not enough arguments for format string`

**Description:**

*Used when a format string that uses unnamed conversion specifiers is given too few arguments*

**Problematic code:**

```
print("Today is {0}, so tomorrow will be {1}".format("Monday"))  # [too-few-format-args]
```

**Correct code:**

```
print("Today is {0}, so tomorrow will be {1}".format("Monday", "Tuesday"))
```

**Related links:**

- [String Formatting](https://docs.python.org/3/library/string.html#formatstrings)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.