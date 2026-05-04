---
id: pylint-W0212
rule_code: "W0212"
rule_name: "protected-access"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/protected-access.html"
---
# protected-access / W0212

**Message emitted:**

`Access to a protected member %s of a client class`

**Description:**

*Used when a protected member (i.e. class member with a name beginning with an underscore) is accessed outside the class or a descendant of the class where it's defined.*

**Problematic code:**

```
class Worm:
    def __swallow(self):
        pass

jim = Worm()
jim.__swallow()  # [protected-access]
```

**Correct code:**

```
class Worm:
    def __swallow(self):
        pass

    def eat(self):
        return self.__swallow()

jim = Worm()
jim.eat()
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.