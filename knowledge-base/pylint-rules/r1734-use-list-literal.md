---
id: pylint-R1734
rule_code: "R1734"
rule_name: "use-list-literal"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/use-list-literal.html"
---
# use-list-literal / R1734

**Message emitted:**

`Consider using [] instead of list()`

**Description:**

*Emitted when using list() to create an empty list instead of the literal []. The literal is faster as it avoids an additional function call.*

**Problematic code:**

```
empty_list = list()  # [use-list-literal]
```

**Correct code:**

```
empty_list = []
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.