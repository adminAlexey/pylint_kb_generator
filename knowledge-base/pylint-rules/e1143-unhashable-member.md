---
id: pylint-E1143
rule_code: "E1143"
rule_name: "unhashable-member"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/unhashable-member.html"
---
# unhashable-member / E1143

**Message emitted:**

`'%s' is unhashable and can't be used as a %s in a %s`

**Description:**

*Emitted when a dict key or set member is not hashable (i.e. doesn't define __hash__ method).*

**Problematic code:**

```
# Print the number of apples:
print({"apple": 42}[["apple"]])  # [unhashable-member]
```

**Correct code:**

```
# Print the number of apples:
print({"apple": 42}["apple"])
```

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.