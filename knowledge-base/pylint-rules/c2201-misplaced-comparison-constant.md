---
id: pylint-C2201
rule_code: "C2201"
rule_name: "misplaced-comparison-constant"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/misplaced-comparison-constant.html"
---
# misplaced-comparison-constant / C2201

**Message emitted:**

`Comparison should be %s`

**Description:**

*Used when the constant is placed on the left side of a comparison. It is usually clearer in intent to place it in the right hand side of the comparison.*

**Problematic code:**

```
def compare_apples(apples=20):
    for i in range(10):
        if 5 <= i:  # [misplaced-comparison-constant]
            pass
        if 1 == i:  # [misplaced-comparison-constant]
            pass
        if 20 < len(apples):  # [misplaced-comparison-constant]
            pass
```

**Correct code:**

```
def compare_apples(apples=20):
    for i in range(10):
        if i >= 5:
            pass
        if i == 1:
            pass
        if len(apples) > 20:
            pass
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.comparison_placement
```

Note

This message is emitted by the optional ['comparison-placement'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-comparison-placement)
checker, which requires the `pylint.extensions.comparison_placement` plugin to be loaded.

Created by the [comparison-placement](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/comparison_placement.py) checker.