---
id: pylint-W1303
rule_code: "W1303"
rule_name: "missing-format-argument-key"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/missing-format-argument-key.html"
---
# missing-format-argument-key / W1303

**Message emitted:**

`Missing keyword argument %r for format string`

**Description:**

*Used when a PEP 3101 format string that uses named fields doesn't receive one or more required keywords.*

**Problematic code:**

```
print("My name is {first} {last}".format(first="John"))  # [missing-format-argument-key]
```

**Correct code:**

```
print("My name is {first} {last}".format(first="John", last="Wick"))
```

**Related links:**

- [PEP 3101](https://peps.python.org/pep-3101/)
- [Custom String Formatting](https://docs.python.org/3/library/string.html#custom-string-formatting)

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.