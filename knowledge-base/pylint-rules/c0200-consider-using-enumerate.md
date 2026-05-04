---
id: pylint-C0200
rule_code: "C0200"
rule_name: "consider-using-enumerate"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/consider-using-enumerate.html"
---
# consider-using-enumerate / C0200

**Message emitted:**

`Consider using enumerate instead of iterating with range and len`

**Description:**

*Emitted when code that iterates with range and len is encountered. Such code can be simplified by using the enumerate builtin.*

**Problematic code:**

```
seasons = ["Spring", "Summer", "Fall", "Winter"]

for i in range(len(seasons)):  # [consider-using-enumerate]
    print(i, seasons[i])
```

**Correct code:**

```
seasons = ["Spring", "Summer", "Fall", "Winter"]

for i, season in enumerate(seasons):
    print(i, season)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/recommendation_checker.py) checker.