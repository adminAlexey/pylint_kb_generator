---
id: pylint-C0121
rule_code: "C0121"
rule_name: "singleton-comparison"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/singleton-comparison.html"
---
# singleton-comparison / C0121

**Message emitted:**

`Comparison %s should be %s`

**Description:**

*Used when an expression is compared to singleton values like True, False or None.*

**Problematic code:**

```
game_won = True
if game_won == True:  # [singleton-comparison]
    print("Game won !")
```

**Correct code:**

```
game_won = True
if game_won:
    print("Game won !")
```

**Related links:**

- [PEP 285 – Adding a bool type](https://peps.python.org/pep-0285/)

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/comparison_checker.py) checker.