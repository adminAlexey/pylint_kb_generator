---
id: pylint-C3401
rule_code: "C3401"
rule_name: "dict-init-mutate"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/dict-init-mutate.html"
---
# dict-init-mutate / C3401

**Message emitted:**

`Declare all known key/values when initializing the dictionary: %s`

**Description:**

*Dictionaries can be initialized with a single statement using dictionary literal syntax.*

**Problematic code:**

```
fruit_prices = {}  # [dict-init-mutate]
fruit_prices["apple"] = 1
fruit_prices["banana"] = 10
```

**Correct code:**

```
fruit_prices = {"apple": 1, "banana": 10}
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.dict_init_mutate,
```

Note

This message is emitted by the optional ['dict-init-mutate'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-dict-init-mutate)
checker, which requires the `pylint.extensions.dict_init_mutate` plugin to be loaded.

Created by the [dict-init-mutate](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/dict_init_mutate.py) checker.