---
id: pylint-E0100
rule_code: "E0100"
rule_name: "init-is-generator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/init-is-generator.html"
---
# init-is-generator / E0100

**Message emitted:**

`__init__ method is a generator`

**Description:**

*Used when the special class method __init__ is turned into a generator by a yield in its body.*

**Problematic code:**

```
class Fruit:
    def __init__(self, worms):  # [init-is-generator]
        yield from worms

apple = Fruit(["Fahad", "Anisha", "Tabatha"])
```

**Correct code:**

```
class Fruit:
    def __init__(self, worms):
        self.__worms = worms

    def worms(self):
        yield from self.__worms

apple = Fruit(["Fahad", "Anisha", "Tabatha"])
for worm in apple.worms():
    pass
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_error_checker.py) checker.