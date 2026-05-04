---
id: pylint-R1729
rule_code: "R1729"
rule_name: "use-a-generator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/use-a-generator.html"
---
# use-a-generator / R1729

**Message emitted:**

`Use a generator instead '%s(%s)'`

**Description:**

*Comprehension inside of 'any', 'all', 'max', 'min' or 'sum' is unnecessary. A generator would be sufficient and faster.*

**Problematic code:**

```
from random import randint

all([randint(-5, 5) > 0 for _ in range(10)])  # [use-a-generator]
any([randint(-5, 5) > 0 for _ in range(10)])  # [use-a-generator]
```

**Correct code:**

```
from random import randint

all(randint(-5, 5) > 0 for _ in range(10))
any(randint(-5, 5) > 0 for _ in range(10))
```

**Additional details:**

By using a generator you can cut the execution tree and exit directly at the first element that is `False` for `all` or `True` for `any` instead of
calculating all the elements. Except in the worst possible case where you still need to evaluate everything (all values
are True for `all` or all values are false for `any`) performance will be better.

**Related links:**

- [PEP 289 – Generator Expressions](https://peps.python.org/pep-0289/)
- [Benchmark and discussion during initial implementation](https://github.com/pylint-dev/pylint/pull/3309#discussion_r576683109)

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.