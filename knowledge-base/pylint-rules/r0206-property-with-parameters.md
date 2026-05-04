---
id: pylint-R0206
rule_code: "R0206"
rule_name: "property-with-parameters"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/property-with-parameters.html"
---
# property-with-parameters / R0206

**Message emitted:**

`Cannot have defined parameters for properties`

**Description:**

*Used when we detect that a property also has parameters, which are useless, given that properties cannot be called with additional arguments.*

**Problematic code:**

```
class Worm:
    @property
    def bore(self, depth):  # [property-with-parameters]
        pass
```

**Correct code:**

```
class Worm:
    @property
    def bore(self):
        """Property accessed with '.bore'."""
        pass

    def bore_with_depth(depth):
        """Function called with .bore_with_depth(depth)."""
        pass
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.