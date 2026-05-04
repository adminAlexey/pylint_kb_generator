---
id: pylint-R3501
rule_code: "R3501"
rule_name: "consider-refactoring-into-while-condition"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-refactoring-into-while-condition.html"
---
# consider-refactoring-into-while-condition / R3501

**Message emitted:**

`Consider using 'while %s' instead of 'while %s:' an 'if', and a 'break'`

**Description:**

*Emitted when `while True:` loop is used and the first statement is a break condition. The ``if / break`` construct can be removed if the check is inverted and moved to the ``while`` statement.*

**Problematic code:**

```
fruit_basket = ["apple", "orange", "banana", "cherry", "guava"]

while True:  # [consider-refactoring-into-while-condition]
    if len(fruit_basket) == 0:
        break
    fruit = fruit_basket.pop()
    print(f"We removed {fruit} from the basket")
```

**Correct code:**

```
fruit_basket = ["apple", "orange", "banana", "cherry", "guava"]

while len(fruit_basket) != 0:
    fruit = fruit_basket.pop()
    print(f"We removed {fruit} from the basket")
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.consider_refactoring_into_while_condition
```

Note

This message is emitted by the optional ['consider_refactoring_into_while'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-consider-refactoring-into-while-condition)
checker, which requires the `pylint.extensions.consider_refactoring_into_while_condition` plugin to be loaded.

Created by the [consider_refactoring_into_while](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/consider_refactoring_into_while_condition.py) checker.