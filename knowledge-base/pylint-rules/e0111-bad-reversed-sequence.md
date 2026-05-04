---
id: pylint-E0111
rule_code: "E0111"
rule_name: "bad-reversed-sequence"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-reversed-sequence.html"
---
# bad-reversed-sequence / E0111

**Message emitted:**

`The first reversed() argument is not a sequence`

**Description:**

*Used when the first argument to reversed() builtin isn't a sequence (does not implement __reversed__, nor __getitem__ and __len__*

**Problematic code:**

```
reversed({1, 2, 3, 4})  # [bad-reversed-sequence]
```

**Correct code:**

```
reversed([1, 2, 3, 4])
```

Created by the [basic](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/base/basic_checker.py) checker.