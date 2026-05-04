---
id: pylint-E1300
rule_code: "E1300"
rule_name: "bad-format-character"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-format-character.html"
---
# bad-format-character / E1300

**Message emitted:**

`Unsupported format character %r (%#02x) at index %d`

**Description:**

*Used when an unsupported format character is used in a format string.*

**Problematic code:**

```
print("%s %z" % ("hello", "world"))  # [bad-format-character]
```

**Correct code:**

```
print("%s %s" % ("hello", "world"))
```

**Additional details:**

This check is currently only active for "old-style" string formatting as seen in the examples.
See [Issue #6085](https://github.com/pylint-dev/pylint/issues/6085) for more information.

**Related links:**

- [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
- [PyFormat](https://pyformat.info/)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.