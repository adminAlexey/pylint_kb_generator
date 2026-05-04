---
id: pylint-R1703
rule_code: "R1703"
rule_name: "simplifiable-if-statement"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/simplifiable-if-statement.html"
---
# simplifiable-if-statement / R1703

**Message emitted:**

`The if statement can be replaced with %s`

**Description:**

*Used when an if statement can be replaced with 'bool(test)'.*

**Problematic code:**

```
FLYING_THINGS = ["bird", "plane", "superman", "this example"]

def is_flying_animal(an_object):
    # +1: [simplifiable-if-statement]
    if isinstance(an_object, Animal) and an_object in FLYING_THINGS:
        is_flying = True
    else:
        is_flying = False
    return is_flying
```

**Correct code:**

```
FLYING_THINGS = ["bird", "plane", "superman", "this example"]

def is_flying_animal(an_object):
    is_flying = isinstance(an_object, Animal) and an_object.name in FLYING_THINGS
    return is_flying
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.