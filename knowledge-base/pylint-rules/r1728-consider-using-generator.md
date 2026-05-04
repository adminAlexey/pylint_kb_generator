---
id: pylint-R1728
rule_code: "R1728"
rule_name: "consider-using-generator"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-generator.html"
---
# consider-using-generator / R1728

**Message emitted:**

`Consider using a generator instead '%s(%s)'`

**Description:**

*If your container can be large using a generator will bring better performance.*

**Problematic code:**

```
list([0 for y in list(range(10))])  # [consider-using-generator]
tuple([0 for y in list(range(10))])  # [consider-using-generator]
sum([y**2 for y in list(range(10))])  # [consider-using-generator]
max([y**2 for y in list(range(10))])  # [consider-using-generator]
min([y**2 for y in list(range(10))])  # [consider-using-generator]
```

**Correct code:**

```
list(0 for y in list(range(10)))
tuple(0 for y in list(range(10)))
sum(y**2 for y in list(range(10)))
max(y**2 for y in list(range(10)))
min(y**2 for y in list(range(10)))
```

**Additional details:**

Removing `[]` inside calls that can use containers or generators should be considered
for performance reasons since a generator will have an upfront cost to pay. The
performance will be better if you are working with long lists or sets.

For `max`, `min` and `sum` using a generator is also recommended by pep289.

**Related links:**

- [PEP 289](https://peps.python.org/pep-0289/)
- [Benchmark and discussion for any/all/list/tuple](https://github.com/pylint-dev/pylint/pull/3309#discussion_r576683109)
- [Benchmark and discussion for sum/max/min](https://github.com/pylint-dev/pylint/pull/6595#issuecomment-1125704244)

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/refactoring_checker.py) checker.