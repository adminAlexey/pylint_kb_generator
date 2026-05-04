---
id: pylint-R1736
rule_code: "R1736"
rule_name: "unnecessary-list-index-lookup"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/unnecessary-list-index-lookup.html"
---
# unnecessary-list-index-lookup / R1736

**Message emitted:**

`Unnecessary list index lookup, use '%s' instead`

**Description:**

*Emitted when iterating over an enumeration and accessing the value by index lookup. The value can be accessed directly instead.*

**Problematic code:**

```
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(letters[index])  # [unnecessary-list-index-lookup]
```

**Correct code:**

```
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(letter)
```

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.