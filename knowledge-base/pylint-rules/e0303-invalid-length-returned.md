---
id: pylint-E0303
rule_code: "E0303"
rule_name: "invalid-length-returned"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/invalid-length-returned.html"
---
# invalid-length-returned / E0303

**Message emitted:**

`__len__ does not return non-negative integer`

**Description:**

*Used when a __len__ method returns something which is not a non-negative integer*

**Problematic code:**

```
class FruitBasket:
    def __init__(self, fruits):
        self.fruits = ["Apple", "Banana", "Orange"]

    def __len__(self):  # [invalid-length-returned]
        return -len(self.fruits)
```

**Correct code:**

```
class FruitBasket:
    def __init__(self, fruits):
        self.fruits = ["Apple", "Banana", "Orange"]

    def __len__(self):
        return len(self.fruits)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/special_methods_checker.py) checker.