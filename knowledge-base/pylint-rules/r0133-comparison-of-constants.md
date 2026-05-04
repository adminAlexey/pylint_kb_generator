---
id: pylint-R0133
rule_code: "R0133"
rule_name: "comparison-of-constants"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/comparison-of-constants.html"
---
# comparison-of-constants / R0133

**Message emitted:**

`Comparison between constants: "%s %s %s" has a constant value`

**Description:**

*When two literals are compared with each other the result is a constant. Using the constant directly is both easier to read and more performant. Initializing 'True' and 'False' this way is not required since Python 2.3.*

**Problematic code:**

```
def is_the_answer() -> bool:
    return 42 == 42  # [comparison-of-constants]
```

**Correct code:**

```
def is_the_answer(meaning_of_life: int) -> bool:
    return meaning_of_life == 42
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.