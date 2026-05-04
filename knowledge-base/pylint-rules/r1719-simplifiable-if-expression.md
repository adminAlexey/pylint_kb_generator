---
id: pylint-R1719
rule_code: "R1719"
rule_name: "simplifiable-if-expression"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/simplifiable-if-expression.html"
---
# simplifiable-if-expression / R1719

**Message emitted:**

`The if expression can be replaced with %s`

**Description:**

*Used when an if expression can be replaced with 'bool(test)' or simply 'test' if the boolean cast is implicit.*

**Problematic code:**

```
FLYING_THINGS = ["bird", "plane", "superman", "this example"]

def is_flying_thing(an_object):
    return True if an_object in FLYING_THINGS else False  # [simplifiable-if-expression]

def is_not_flying_thing(an_object):
    return False if an_object in FLYING_THINGS else True  # [simplifiable-if-expression]
```

**Correct code:**

```
FLYING_THINGS = ["bird", "plane", "superman", "this example"]

def is_flying_thing(an_object):
    return an_object in FLYING_THINGS

def is_not_flying_thing(an_object):
    return an_object not in FLYING_THINGS
```

**Related links:**

- [Simplifying an 'if' statement with bool()](https://stackoverflow.com/questions/49546992/)

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.