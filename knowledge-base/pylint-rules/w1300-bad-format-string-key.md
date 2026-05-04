---
id: pylint-W1300
rule_code: "W1300"
rule_name: "bad-format-string-key"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-format-string-key.html"
---
# bad-format-string-key / W1300

**Message emitted:**

`Format string dictionary key should be a string, not %s`

**Description:**

*Used when a format string that uses named conversion specifiers is used with a dictionary whose keys are not all strings.*

**Problematic code:**

```
print("%(one)d" % {"one": 1, 2: 2})  # [bad-format-string-key]
```

**Correct code:**

```
print("%(one)d, %(two)d" % {"one": 1, "two": 2})
```

**Additional details:**

This check only works for old-style string formatting using the '%' operator.

This check only works if the dictionary with the values to be formatted is defined inline.
Passing a variable will not trigger the check as the other keys in this dictionary may be
used in other contexts, while an inline defined dictionary is clearly only intended to hold
the values that should be formatted.

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.