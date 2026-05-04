---
id: pylint-E0203
rule_code: "E0203"
rule_name: "access-member-before-definition"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/access-member-before-definition.html"
---
# access-member-before-definition / E0203

**Message emitted:**

`Access to member %r before its definition line %s`

**Description:**

*Used when an instance member is accessed before it's actually assigned.*

**Problematic code:**

```
class Unicorn:
    def __init__(self, fluffiness_level):
        if self.fluffiness_level > 9000:  # [access-member-before-definition]
            print("It's OVER-FLUFFYYYY ! *crush glasses*")
        self.fluffiness_level = fluffiness_level
```

**Correct code:**

```
class Unicorn:
    def __init__(self, fluffiness_level):
        self.fluffiness_level = fluffiness_level
        if self.fluffiness_level > 9000:
            print("It's OVER-FLUFFYYYY ! *crush glasses*")
```

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.