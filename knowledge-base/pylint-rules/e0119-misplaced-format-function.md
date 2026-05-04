---
id: pylint-E0119
rule_code: "E0119"
rule_name: "misplaced-format-function"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/misplaced-format-function.html"
---
# misplaced-format-function / E0119

**Message emitted:**

`format function is not called on str`

**Description:**

*Emitted when format function is not called on str object. e.g doing print("value: {}").format(123) instead of print("value: {}".format(123)). This might not be what the user intended to do.*

**Problematic code:**

```
print("Value: {}").format("Car")  # [misplaced-format-function]
```

**Correct code:**

```
print("Value: {}".format("Car"))
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.