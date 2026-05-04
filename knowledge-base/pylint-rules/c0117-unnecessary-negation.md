---
id: pylint-C0117
rule_code: "C0117"
rule_name: "unnecessary-negation"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unnecessary-negation.html"
---
# unnecessary-negation / C0117

**Message emitted:**

`Consider changing "%s" to "%s"`

**Description:**

*Used when a boolean expression contains an unneeded negation, e.g. when two negation operators cancel each other out.*

**Problematic code:**

`double_not.py`:

```
if not not input():  # [unnecessary-negation]
    pass
```

`equivalent_comparator_exists.py`:

```
a = 3
b = 10
if not a > b:  # [unnecessary-negation]
    pass
```

**Correct code:**

`double_not.py`:

```
if input():
    pass
```

`equivalent_comparator_exists.py`:

```
a = 3
b = 10
if a <= b:
    pass
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/not_checker.py) checker.