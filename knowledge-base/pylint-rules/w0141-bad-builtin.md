---
id: pylint-W0141
rule_code: "W0141"
rule_name: "bad-builtin"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bad-builtin.html"
---
# bad-builtin / W0141

**Message emitted:**

`Used builtin function %s`

**Description:**

*Used when a disallowed builtin function is used (see the bad-function option). Usual disallowed functions are the ones like map, or filter , where Python offers now some cleaner alternative like list comprehension.*

**Problematic code:**

```
numbers = list(map(lambda x: 2 * x, [1, 2, 3]))  # [bad-builtin]
print(numbers)
```

**Correct code:**

```
numbers = [2 * x for x in [1, 2, 3]]
print(numbers)
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.bad_builtin
```

Note

This message is emitted by the optional ['deprecated_builtins'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-bad-builtin)
checker, which requires the `pylint.extensions.bad_builtin` plugin to be loaded.

Created by the [deprecated_builtins](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/bad_builtin.py) checker.