---
id: pylint-E1303
rule_code: "E1303"
rule_name: "format-needs-mapping"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/format-needs-mapping.html"
---
# format-needs-mapping / E1303

**Message emitted:**

`Expected mapping for format string, not %s`

**Description:**

*Used when a format string that uses named conversion specifiers is used with an argument that is not a mapping.*

**Problematic code:**

```
print("%(x)d %(y)d" % [1, 2])  # [format-needs-mapping]
```

**Correct code:**

```
print("%(x)d %(y)d" % {"x": 1, "y": 2})
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.