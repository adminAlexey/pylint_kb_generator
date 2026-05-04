---
id: pylint-E1141
rule_code: "E1141"
rule_name: "dict-iter-missing-items"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/dict-iter-missing-items.html"
---
# dict-iter-missing-items / E1141

**Message emitted:**

`Unpacking a dictionary in iteration without calling .items()`

**Description:**

*Emitted when trying to iterate through a dict without calling .items()*

**Problematic code:**

```
data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}
for city, population in data:  # [dict-iter-missing-items]
    print(f"{city} has population {population}.")
```

**Correct code:**

```
data = {"Paris": 2_165_423, "New York City": 8_804_190, "Tokyo": 13_988_129}
for city, population in data.items():
    print(f"{city} has population {population}.")
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.