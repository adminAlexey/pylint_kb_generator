---
id: pylint-E1301
rule_code: "E1301"
rule_name: "truncated-format-string"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/truncated-format-string.html"
---
# truncated-format-string / E1301

**Message emitted:**

`Format string ends in middle of conversion specifier`

**Description:**

*Used when a format string terminates before the end of a conversion specifier.*

**Problematic code:**

```
PARG_2 = 1

print("strange format %2" % PARG_2)  # [truncated-format-string]
```

**Correct code:**

```
PARG_2 = 1

print(f"strange format {PARG_2}")
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.