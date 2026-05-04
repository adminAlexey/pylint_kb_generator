---
id: pylint-W0245
rule_code: "W0245"
rule_name: "super-without-brackets"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/super-without-brackets.html"
---
# super-without-brackets / W0245

**Message emitted:**

`Super call without brackets`

**Description:**

*Used when a call to super does not have brackets and thus is not an actual call and does not work as expected.*

**Problematic code:**

```
class Soup:
    @staticmethod
    def temp():
        print("Soup is hot!")

class TomatoSoup(Soup):
    @staticmethod
    def temp():
        super.temp()  # [super-without-brackets]
        print("But tomato soup is even hotter!")
```

**Correct code:**

```
class Soup:
    @staticmethod
    def temp():
        print("Soup is hot!")

class TomatoSoup(Soup):
    @staticmethod
    def temp():
        super().temp()
        print("But tomato soup is even hotter!")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.