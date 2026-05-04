---
id: pylint-R0124
rule_code: "R0124"
rule_name: "comparison-with-itself"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/comparison-with-itself.html"
---
# comparison-with-itself / R0124

**Message emitted:**

`Redundant comparison - %s`

**Description:**

*Used when something is compared against itself.*

**Problematic code:**

```
def is_an_orange(fruit):
    an_orange = "orange"
    return fruit == fruit  # [comparison-with-itself]
```

**Correct code:**

```
def is_an_orange(fruit):
    an_orange = "orange"
    return an_orange == fruit
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.