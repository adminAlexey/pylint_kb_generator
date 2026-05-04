---
id: pylint-W0199
rule_code: "W0199"
rule_name: "assert-on-tuple"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/assert-on-tuple.html"
---
# assert-on-tuple / W0199

**Message emitted:**

`Assert called on a populated tuple. Did you mean 'assert x,y'?`

**Description:**

*A call of assert on a tuple will always evaluate to true if the tuple is not empty, and will always evaluate to false if it is.*

**Problematic code:**

```
assert (1, None)  # [assert-on-tuple]
```

**Correct code:**

```
x, y = (1, None)
assert x
assert y
```

**Additional details:**

**Directly asserting a non-empty tuple will always pass. The solution is to**
: test something that could fail, or not assert at all.Forunittestassertions there is the similarredundant-unittest-assert / W1503message.

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.