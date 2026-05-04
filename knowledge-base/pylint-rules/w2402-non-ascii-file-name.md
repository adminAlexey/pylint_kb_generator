---
id: pylint-W2402
rule_code: "W2402"
rule_name: "non-ascii-file-name"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/non-ascii-file-name.html"
---
# non-ascii-file-name / W2402

**Message emitted:**

`%s name "%s" contains a non-ASCII character.`

**Description:**

*Under python 3.5, PEP 3131 allows non-ascii identifiers, but not non-ascii file names.Since Python 3.5, even though Python supports UTF-8 files, some editors or tools don't.*

**Problematic code:**

`bàd.py`:

```
# [non-ascii-file-name]
```

`not_bétter.py`:

```
# [non-ascii-file-name]
```

**Correct code:**

`__init__.py`:

```

```

`bad.py`:

```

```

`not_better.py`:

```

```

**Related links:**

- [PEP 489](https://peps.python.org/pep-0489/#export-hook-name)
- [PEP 672](https://peps.python.org/pep-0672/#confusing-features)
- [Python issue 20485](https://bugs.python.org/issue20485)

Created by the [nonascii-checker](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/non_ascii_names.py) checker.