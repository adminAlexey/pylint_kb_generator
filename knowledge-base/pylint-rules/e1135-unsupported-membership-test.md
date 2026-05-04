---
id: pylint-E1135
rule_code: "E1135"
rule_name: "unsupported-membership-test"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unsupported-membership-test.html"
---
# unsupported-membership-test / E1135

**Message emitted:**

`Value '%s' doesn't support membership test`

**Description:**

*Emitted when an instance in membership test expression doesn't implement membership protocol (__contains__/__iter__/__getitem__).*

**Problematic code:**

```
class Fruit:
    pass

apple = "apple" in Fruit()  # [unsupported-membership-test]
```

**Correct code:**

```
class Fruit:
    FRUITS = ["apple", "orange"]

    def __contains__(self, name):
        return name in self.FRUITS

apple = "apple" in Fruit()
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.