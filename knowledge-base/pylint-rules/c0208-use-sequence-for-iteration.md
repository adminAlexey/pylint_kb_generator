---
id: pylint-C0208
rule_code: "C0208"
rule_name: "use-sequence-for-iteration"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/use-sequence-for-iteration.html"
---
# use-sequence-for-iteration / C0208

**Message emitted:**

`Use a sequence type when iterating over values`

**Description:**

*When iterating over values, sequence types (e.g., ``lists``, ``tuples``, ``ranges``) are more efficient than ``sets``.*

**Problematic code:**

```
for food in {"apples", "lemons", "water"}:  # [use-sequence-for-iteration]
    print(f"I like {food}.")
```

**Correct code:**

`list.py`:

```
for food in ["apples", "lemons", "water"]:
    print(f"I like {food}.")
```

`tuple.py`:

```
for food in ("apples", "lemons", "water"):
    print(f"I like {food}.")
```

**Additional details:**

[https://gist.github.com/hofrob/8b1c1e205a0d4c66a680b1fe4bfeba11](https://gist.github.com/hofrob/8b1c1e205a0d4c66a680b1fe4bfeba11)

This example script shows a significant increase in performance when using a list, tuple or range over a set in python version 3.11.1.

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/recommendation_checker.py) checker.