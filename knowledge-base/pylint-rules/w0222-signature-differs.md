---
id: pylint-W0222
rule_code: "W0222"
rule_name: "signature-differs"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/signature-differs.html"
---
# signature-differs / W0222

**Message emitted:**

`Signature differs from %s %r method`

**Description:**

*Used when a method signature is different than in the implemented interface or in an overridden method.*

**Problematic code:**

```
class Animal:
    def run(self, distance=0):
        print(f"Ran {distance} km!")

class Dog(Animal):
    def run(self, distance):  # [signature-differs]
        super(Animal, self).run(distance)
        print("Fetched that stick, wuff !")
```

**Correct code:**

```
class Animal:
    def run(self, distance=0):
        print(f"Ran {distance} km!")

class Dog(Animal):
    def run(self, distance=0):
        super(Animal, self).run(distance)
        print("Fetched that stick, wuff !")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.