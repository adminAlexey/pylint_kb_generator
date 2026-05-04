---
id: pylint-E0710
rule_code: "E0710"
rule_name: "raising-non-exception"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/raising-non-exception.html"
---
# raising-non-exception / E0710

**Message emitted:**

`Raising a class which doesn't inherit from BaseException`

**Description:**

*Used when a class which doesn't inherit from BaseException is raised.*

**Problematic code:**

```
raise str  # [raising-non-exception]
```

**Correct code:**

```
raise Exception("Goodbye world !")
```

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.