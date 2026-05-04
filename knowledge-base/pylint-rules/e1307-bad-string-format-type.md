---
id: pylint-E1307
rule_code: "E1307"
rule_name: "bad-string-format-type"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-string-format-type.html"
---
# bad-string-format-type / E1307

**Message emitted:**

`Argument %r does not match format type %r`

**Description:**

*Used when a type required by format string is not suitable for actual argument type*

**Problematic code:**

```
print("%d" % "1")  # [bad-string-format-type]
```

**Correct code:**

```
print("%d" % 1)
```

**Additional details:**

This check is currently only active for "old-style" string formatting as seen in the examples.
See [Issue #6085](https://github.com/pylint-dev/pylint/issues/6163) for more information.

**Related links:**

- [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
- [PyFormat](https://pyformat.info/)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.