---
id: pylint-E0112
rule_code: "E0112"
rule_name: "too-many-star-expressions"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/too-many-star-expressions.html"
---
# too-many-star-expressions / E0112

**Message emitted:**

`More than one starred expression in assignment`

**Description:**

*Emitted when there are more than one starred expressions (`*x`) in an assignment. This is a SyntaxError.*

**Problematic code:**

```
*stars, *constellations = ["Sirius", "Arcturus", "Vega"]  # [too-many-star-expressions]
```

**Correct code:**

```
*sirius_and_arcturus, vega = ["Sirius", "Arcturus", "Vega"]
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.