---
id: pylint-W0644
rule_code: "W0644"
rule_name: "unbalanced-dict-unpacking"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unbalanced-dict-unpacking.html"
---
# unbalanced-dict-unpacking / W0644

**Message emitted:**

`Possible unbalanced dict unpacking with %s: left side has %d label%s, right side has %d value%s`

**Description:**

*Used when there is an unbalanced dict unpacking in assignment or for loop*

**Problematic code:**

```
FRUITS = {"apple": 2, "orange": 3, "mellon": 10}

for fruit, price in FRUITS.values():  # [unbalanced-dict-unpacking]
    print(fruit)
```

**Correct code:**

```
FRUITS = {"apple": 2, "orange": 3, "mellon": 10}

for fruit, price in FRUITS.items():
    print(fruit)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.