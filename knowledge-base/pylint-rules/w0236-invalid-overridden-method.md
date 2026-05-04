---
id: pylint-W0236
rule_code: "W0236"
rule_name: "invalid-overridden-method"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/invalid-overridden-method.html"
---
# invalid-overridden-method / W0236

**Message emitted:**

`Method %r was expected to be %r, found it instead as %r`

**Description:**

*Used when we detect that a method was overridden in a way that does not match its base class which could result in potential bugs at runtime.*

**Problematic code:**

```
class Fruit:
    async def bore(self, insect):
        insect.eat(self)

class Apple(Fruit):
    def bore(self, insect):  # [invalid-overridden-method]
        insect.eat(self)
```

**Correct code:**

```
class Fruit:
    async def bore(self, insect):
        insect.eat(self)

class Apple(Fruit):
    async def bore(self, insect):
        insect.eat(self)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.