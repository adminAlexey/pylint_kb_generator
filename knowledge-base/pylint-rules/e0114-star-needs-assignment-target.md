---
id: pylint-E0114
rule_code: "E0114"
rule_name: "star-needs-assignment-target"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/star-needs-assignment-target.html"
---
# star-needs-assignment-target / E0114

**Message emitted:**

`Can use starred expression only in assignment target`

**Description:**

*Emitted when a star expression is not used in an assignment target.*

**Problematic code:**

```
stars = *["Sirius", "Arcturus", "Vega"]  # [star-needs-assignment-target]
```

**Correct code:**

```
sirius, *arcturus_and_vega = ["Sirius", "Arcturus", "Vega"]
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.