---
id: pylint-R1716
rule_code: "R1716"
rule_name: "chained-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/chained-comparison.html"
---
# chained-comparison / R1716

**Message emitted:**

`Simplify chained comparison between the operands`

**Description:**

*This message is emitted when pylint encounters boolean operation like "a < b and b < c", suggesting instead to refactor it to "a < b < c"*

**Problematic code:**

```
a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:  # [chained-comparison]
    pass
```

**Correct code:**

```
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    pass
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.