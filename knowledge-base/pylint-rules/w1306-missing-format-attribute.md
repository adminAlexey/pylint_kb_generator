---
id: pylint-W1306
rule_code: "W1306"
rule_name: "missing-format-attribute"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-format-attribute.html"
---
# missing-format-attribute / W1306

**Message emitted:**

`Missing format attribute %r in format specifier %r`

**Description:**

*Used when a PEP 3101 format string uses an attribute specifier ({0.length}), but the argument passed for formatting doesn't have that attribute.*

**Problematic code:**

```
print("{0.real}".format("1"))  # [missing-format-attribute]
```

**Correct code:**

```
print("{0.real}".format(1))
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.