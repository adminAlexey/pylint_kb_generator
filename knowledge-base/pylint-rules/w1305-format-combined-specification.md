---
id: pylint-W1305
rule_code: "W1305"
rule_name: "format-combined-specification"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/format-combined-specification.html"
---
# format-combined-specification / W1305

**Message emitted:**

`Format string contains both automatic field numbering and manual field specification`

**Description:**

*Used when a PEP 3101 format string contains both automatic field numbering (e.g. '{}') and manual field specification (e.g. '{0}').*

**Problematic code:**

```
print("{} {1}".format("hello", "world"))  # [format-combined-specification]
```

**Correct code:**

`index_formatting.py`:

```
print("{0} {1}".format("hello", "world"))
```

`order_formatting.py`:

```
print("{} {}".format("hello", "world"))
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.