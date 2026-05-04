---
id: pylint-C1802
rule_code: "C1802"
rule_name: "use-implicit-booleaness-not-len"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/use-implicit-booleaness-not-len.html"
---
# use-implicit-booleaness-not-len / C1802

**Message emitted:**

`Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty`

**Description:**

*Empty sequences are considered false in a boolean context. You can either remove the call to 'len' (``if not x``) or compare the length against a scalar (``if len(x) > 1``).*

**Problematic code:**

```
fruits = ["orange", "apple"]

if len(fruits):  # [use-implicit-booleaness-not-len]
    print(fruits)
```

**Correct code:**

```
fruits = ["orange", "apple"]

if fruits:
    print(fruits)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/implicit_booleaness_checker.py) checker.