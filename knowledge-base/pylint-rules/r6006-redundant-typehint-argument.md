---
id: pylint-R6006
rule_code: "R6006"
rule_name: "redundant-typehint-argument"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/redundant-typehint-argument.html"
---
# redundant-typehint-argument / R6006

**Message emitted:**

`Type `%s` is used more than once in union type annotation. Remove redundant typehints.`

**Description:**

*Duplicated type arguments will be skipped by `mypy` tool, therefore should be removed to avoid confusion.*

**Problematic code:**

```
from typing import Union

sweet_count: Union[int, str, int] = 42  # [redundant-typehint-argument]
```

**Correct code:**

```
from typing import Union

sweet_count: Union[str, int] = 42
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.typing
```

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.