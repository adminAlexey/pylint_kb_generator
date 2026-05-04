---
id: pylint-W0238
rule_code: "W0238"
rule_name: "unused-private-member"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unused-private-member.html"
---
# unused-private-member / W0238

**Message emitted:**

`Unused private member `%s.%s``

**Description:**

*Emitted when a private member of a class is defined but not used.*

**Problematic code:**

```
class Fruit:
    FRUITS = {"apple": "red", "orange": "orange"}

    def __print_color(self):  # [unused-private-member]
        pass
```

**Correct code:**

```
class Fruit:
    FRUITS = {"apple": "red", "orange": "orange"}

    def __print_color(self, name, color):
        print(f"{name}: {color}")

    def print(self):
        for fruit, color in self.FRUITS.items():
            self.__print_color(fruit, color)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.