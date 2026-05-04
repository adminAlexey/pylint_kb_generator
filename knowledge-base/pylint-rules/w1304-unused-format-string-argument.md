---
id: pylint-W1304
rule_code: "W1304"
rule_name: "unused-format-string-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-format-string-argument.html"
---
# unused-format-string-argument / W1304

**Message emitted:**

`Unused format argument %r`

**Description:**

*Used when a PEP 3101 format string that uses named fields is used with an argument that is not required by the format string.*

**Problematic code:**

```
print("{x} {y}".format(x=1, y=2, z=3))  # [unused-format-string-argument]
```

**Correct code:**

`add_format_target.py`:

```
print("{x} {y} {z}".format(x=1, y=2, z=3))
```

`remove_unused_args.py`:

```
print("{x} {y}".format(x=1, y=2))
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.