---
id: pylint-R0123
rule_code: "R0123"
rule_name: "literal-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/literal-comparison.html"
---
# literal-comparison / R0123

**Message emitted:**

`In '%s', use '%s' when comparing constant literals not '%s' ('%s')`

**Description:**

*Used when comparing an object to a literal, which is usually what you do not want to do, since you can compare to a different literal than what was expected altogether.*

**Problematic code:**

```
def is_an_orange(fruit):
    return fruit is "orange"  # [literal-comparison]
```

**Correct code:**

```
def is_an_orange(fruit):
    return fruit == "orange"
```

**Related links:**

- [Comparison operations in Python](https://docs.python.org/3/library/stdtypes.html#comparisons)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.