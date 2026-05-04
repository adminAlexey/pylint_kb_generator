---
id: pylint-R1715
rule_code: "R1715"
rule_name: "consider-using-get"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-get.html"
---
# consider-using-get / R1715

**Message emitted:**

`Consider using dict.get for getting values from a dict if a key is present or a default if not`

**Description:**

*Using the builtin dict.get for getting a value from a dictionary if a key is present or a default if not, is simpler and considered more idiomatic, although sometimes a bit slower*

**Problematic code:**

```
knights = {"Gallahad": "the pure", "Robin": "the brave"}

if "Gallahad" in knights:  # [consider-using-get]
    DESCRIPTION = knights["Gallahad"]
else:
    DESCRIPTION = ""
```

**Correct code:**

```
knights = {"Gallahad": "the pure", "Robin": "the brave"}

description = knights.get("Gallahad", "")
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.