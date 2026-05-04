---
id: pylint-E1302
rule_code: "E1302"
rule_name: "mixed-format-string"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/mixed-format-string.html"
---
# mixed-format-string / E1302

**Message emitted:**

`Mixing named and unnamed conversion specifiers in format string`

**Description:**

*Used when a format string contains both named (e.g. '%(foo)d') and unnamed (e.g. '%d') conversion specifiers.  This is also used when a named conversion specifier contains * for the minimum field width and/or precision.*

**Problematic code:**

```
print("x=%(x)d, y=%d" % (0, 1))  # [mixed-format-string]
```

**Correct code:**

`only_named.py`:

```
print("x=%(x)d, y=%(y)d" % {"x": 0, "y": 1})
```

`only_ordered.py`:

```
print("x=%d, y=%d" % (0, 1))
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.