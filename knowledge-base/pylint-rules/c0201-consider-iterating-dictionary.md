---
id: pylint-C0201
rule_code: "C0201"
rule_name: "consider-iterating-dictionary"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/consider-iterating-dictionary.html"
---
# consider-iterating-dictionary / C0201

**Message emitted:**

`Consider iterating the dictionary directly instead of calling .keys()`

**Description:**

*Emitted when the keys of a dictionary are iterated through the ``.keys()`` method or when ``.keys()`` is used for a membership check. It is enough to iterate through the dictionary itself, ``for key in dictionary``. For membership checks, ``if key in dictionary`` is faster.*

**Problematic code:**

```
FRUITS = {"apple": 1, "pear": 5, "peach": 10}

for fruit in FRUITS.keys():  # [consider-iterating-dictionary]
    print(fruit)
```

**Correct code:**

```
FRUITS = {"apple": 1, "pear": 5, "peach": 10}

for fruit in FRUITS:
    print(fruit)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/recommendation_checker.py) checker.