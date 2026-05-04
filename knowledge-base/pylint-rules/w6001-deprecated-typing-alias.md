---
id: pylint-W6001
rule_code: "W6001"
rule_name: "deprecated-typing-alias"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-typing-alias.html"
---
# deprecated-typing-alias / W6001

**Message emitted:**

`'%s' is deprecated, use '%s' instead`

**Description:**

*Emitted when a deprecated typing alias is used.*

**Problematic code:**

```
import typing

item_to_number_of_item: typing.Dict[str, int]  # [deprecated-typing-alias]
```

**Correct code:**

```
item_to_number_of_item: dict[str, int]
```

**Configuration file:**

```
[main]
load-plugins = pylint.extensions.typing
```

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.