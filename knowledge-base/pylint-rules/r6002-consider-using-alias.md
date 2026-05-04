---
id: pylint-R6002
rule_code: "R6002"
rule_name: "consider-using-alias"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-using-alias.html"
---
# consider-using-alias / R6002

**Message emitted:**

`'%s' will be deprecated with PY39, consider using '%s' instead%s`

**Description:**

*Only emitted if 'runtime-typing=no' and a deprecated typing alias is used in a type annotation context in Python 3.7 or 3.8.*

**Problematic code:**

```
import typing

cats: typing.Dict[str, int]  # [consider-using-alias]
```

**Correct code:**

```
import typing

cats: typing.cast(dict[str, int], "string")
```

**Configuration file:**

```
[main]
load-plugins = pylint.extensions.typing
py-version = 3.7
runtime-typing=no
```

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.