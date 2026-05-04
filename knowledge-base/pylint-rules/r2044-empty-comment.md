---
id: pylint-R2044
rule_code: "R2044"
rule_name: "empty-comment"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/empty-comment.html"
---
# empty-comment / R2044

**Message emitted:**

`Line with empty comment`

**Description:**

*Used when a # symbol appears on a line not followed by an actual comment*

**Problematic code:**

```
# +1:[empty-comment]
#

# +1:[empty-comment]
x = 0  #
```

**Correct code:**

```
# comment

x = 0  # comment
```

**Configuration file:**

```
[main]
load-plugins=pylint.extensions.empty_comment
```

Note

This message is emitted by the optional ['empty-comment'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-empty-comment)
checker, which requires the `pylint.extensions.empty_comment` plugin to be loaded.

Created by the [empty-comment](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/empty_comment.py) checker.