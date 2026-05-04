---
id: pylint-R6003
rule_code: "R6003"
rule_name: "consider-alternative-union-syntax"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/consider-alternative-union-syntax.html"
---
# consider-alternative-union-syntax / R6003

**Message emitted:**

`Consider using alternative union syntax instead of '%s'%s`

**Description:**

*Emitted when ``typing.Union`` or ``typing.Optional`` is used instead of the shorthand union syntax. For example, ``Union[int, float]`` instead of ``int | float``. Using the shorthand for unions aligns with Python typing recommendations, removes the need for imports, and avoids confusion in function signatures.*

**Problematic code:**

```
from typing import Optional, Union

def forecast(
    temp: Union[int, float],  # [consider-alternative-union-syntax]
    unit: Optional[str],  # [consider-alternative-union-syntax]
) -> None:
    print(f'Temperature: {temp}{unit or ""}')
```

**Correct code:**

```
def forecast(temp: int | float, unit: str | None) -> None:
    print(f'Temperature: {temp}{unit or ""}')
```

**Configuration file:**

```
[MAIN]
load-plugins = pylint.extensions.typing
```

**Additional details:**

Using the shorthand syntax for union types is [recommended over thetypingmodule](https://docs.python.org/3/library/typing.html#typing.Union). This is consistent with the broader recommendation to prefer built-in types over imports (for example, using `list` instead of the now-deprecated `typing.List`).

`typing.Optional` can also cause confusion in annotated function arguments, since an argument annotated as `Optional` is still a *required* argument when a default value is not set. Explicitly annotating such arguments with `type | None` makes the intention clear.

Note

This message is emitted by the optional ['typing'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-typing)
checker, which requires the `pylint.extensions.typing` plugin to be loaded.

Created by the [typing](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/typing.py) checker.