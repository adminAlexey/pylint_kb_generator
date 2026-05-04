---
id: pylint-C2701
rule_code: "C2701"
rule_name: "import-private-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/import-private-name.html"
---
# import-private-name / C2701

**Message emitted:**

`Imported private %s (%s)`

**Description:**

*Used when a private module or object prefixed with _ is imported. PEP8 guidance on Naming Conventions states that public attributes with leading underscores should be considered private.*

**Problematic code:**

```
from argparse import _AttributeHolder, _SubParsersAction  # [import-private-name]

attr_holder = _AttributeHolder()

def add_sub_parser(sub_parsers: _SubParsersAction):
    sub_parsers.add_parser("my_subparser")
    # ...
```

**Correct code:**

```
"""Private import can be used as type annotations."""

from argparse import _SubParsersAction

def add_sub_parser(sub_parsers: _SubParsersAction):
    sub_parsers.add_parser("my_subparser")
    # ...
```

**Configuration file:**

```
[main]
load-plugins = pylint.extensions.private_import
```

**Additional details:**

Using private imports expose you to unexpected breaking changes for any version
bump of your dependencies, even in patch versions.

Note

This message is emitted by the optional ['import-private-name'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-private-import)
checker, which requires the `pylint.extensions.private_import` plugin to be loaded.

Created by the [import-private-name](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/private_import.py) checker.