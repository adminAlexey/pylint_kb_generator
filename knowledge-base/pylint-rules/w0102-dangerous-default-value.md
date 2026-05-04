---
id: pylint-W0102
rule_code: "W0102"
rule_name: "dangerous-default-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/dangerous-default-value.html"
---
# dangerous-default-value / W0102

**Message emitted:**

`Dangerous default value %s as argument`

**Description:**

*Used when a mutable value as list or dictionary is detected in a default value for an argument.*

**Problematic code:**

```
def whats_on_the_telly(penguin=[]):  # [dangerous-default-value]
    penguin.append("property of the zoo")
    return penguin
```

**Correct code:**

```
def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin
```

**Additional details:**

With a mutable default value, with each call the default value is modified, i.e.:

```
whats_on_the_telly() # ["property of the zoo"]
whats_on_the_telly() # ["property of the zoo", "property of the zoo"]
whats_on_the_telly() # ["property of the zoo", "property of the zoo", "property of the zoo"]
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.