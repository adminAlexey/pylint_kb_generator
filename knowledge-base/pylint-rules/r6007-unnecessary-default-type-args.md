---
id: pylint-R6007
rule_code: "R6007"
rule_name: "unnecessary-default-type-args"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/unnecessary-default-type-args.html"
---
# unnecessary-default-type-args / R6007

**Message emitted:**

`Type `%s` has unnecessary default type args. Change it to `%s`.`

**Description:**

*Emitted when types have default type args which can be omitted. Mainly used for `typing.Generator` and `typing.AsyncGenerator`.*

**Problematic code:**

```
from collections.abc import AsyncGenerator, Generator

a1: AsyncGenerator[int, None]  # [unnecessary-default-type-args]
b1: Generator[int, None, None]  # [unnecessary-default-type-args]
```

**Correct code:**

```
from collections.abc import AsyncGenerator, Generator

a1: AsyncGenerator[int]
b1: Generator[int]
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.typing
```

**Additional details:**

At the moment, this check only works for `Generator` and `AsyncGenerator`.

Starting with Python 3.13, the `SendType` and `ReturnType` default to `None`.
As such it's no longer necessary to specify them. The `collections.abc` variants
don't validate the number of type arguments. Therefore the defaults for these
can be used in earlier versions as well.

**Related links:**

- [Python documentation for AsyncGenerator](https://docs.python.org/3.13/library/typing.html#typing.AsyncGenerator)
- [Python documentation for Generator](https://docs.python.org/3.13/library/typing.html#typing.Generator)

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.