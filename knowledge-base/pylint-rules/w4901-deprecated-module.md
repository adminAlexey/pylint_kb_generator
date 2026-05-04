---
id: pylint-W4901
rule_code: "W4901"
rule_name: "deprecated-module"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/deprecated-module.html"
---
# deprecated-module / W4901

**Message emitted:**

`Deprecated module %r`

**Description:**

*A module marked as deprecated is imported.*

**Problematic code:**

```
import distutils  # [deprecated-module]

import whatever_you_want  # [deprecated-module]
```

**Correct code:**

```
import setuptools
import whatever_replacement_you_want
```

**Configuration file:**

```
[main]
py-version=3.7
deprecated-modules=whatever_you_want
```

**Additional details:**

The actual replacement needs to be studied on a case by case basis
by reading the deprecation warning or the release notes.

Created by the [imports](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/imports.py) checker.