---
id: pylint-W0237
rule_code: "W0237"
rule_name: "arguments-renamed"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/arguments-renamed.html"
---
# arguments-renamed / W0237

**Message emitted:**

`%s %s %r method`

**Description:**

*Used when a method parameter has a different name than in the implemented interface or in an overridden method.*

**Problematic code:**

```
class Fruit:
    def brew(self, ingredient_name: str):
        print(f"Brewing a {type(self)} with {ingredient_name}")

class Apple(Fruit): ...

class Orange(Fruit):
    def brew(self, flavor: str):  # [arguments-renamed]
        print(f"Brewing an orange with {flavor}")

for fruit, ingredient_name in [[Orange(), "thyme"], [Apple(), "cinnamon"]]:
    fruit.brew(ingredient_name=ingredient_name)
```

**Correct code:**

```
class Fruit:
    def brew(self, ingredient_name: str):
        print(f"Brewing a {type(self)} with {ingredient_name}")

class Apple(Fruit): ...

class Orange(Fruit):
    def brew(self, ingredient_name: str):
        print(f"Brewing an orange with {ingredient_name}")

for fruit, ingredient_name in [[Orange(), "thyme"], [Apple(), "cinnamon"]]:
    fruit.brew(ingredient_name=ingredient_name)
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.