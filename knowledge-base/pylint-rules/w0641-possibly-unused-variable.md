---
id: pylint-W0641
rule_code: "W0641"
rule_name: "possibly-unused-variable"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/possibly-unused-variable.html"
---
# possibly-unused-variable / W0641

**Message emitted:**

`Possibly unused variable %r`

**Description:**

*Used when a variable is defined but might not be used. The possibility comes from the fact that locals() might be used, which could consume or not the said variable*

**Problematic code:**

```
def choose_fruits(fruits):
    print(fruits)
    color = "red"  # [possibly-unused-variable]
    return locals()
```

**Correct code:**

```
def choose_fruits(fruits):
    current_locals = locals()
    print(fruits)
    color = "red"
    print(color)
    return current_locals
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.