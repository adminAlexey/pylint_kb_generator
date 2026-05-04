---
id: pylint-W3301
rule_code: "W3301"
rule_name: "nested-min-max"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/nested-min-max.html"
---
# nested-min-max / W3301

**Message emitted:**

`Do not use nested call of '%s'; it's possible to do '%s' instead`

**Description:**

*Nested calls ``min(1, min(2, 3))`` can be rewritten as ``min(1, 2, 3)``.*

**Problematic code:**

```
print(min(1, min(2, 3)))  # [nested-min-max]
```

**Correct code:**

```
print(min(1, 2, 3))
```

Created by the [nested_min_max](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/nested_min_max.py) checker.