---
id: pylint-W0511
rule_code: "W0511"
rule_name: "fixme"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/fixme.html"
---
# fixme / W0511

**Message emitted:**

`%s`

**Description:**

*Used when a warning note as FIXME or XXX is detected.*

**Problematic code:**

```
# TODO: We should fix this at some point  # [fixme]
```

**Correct code:**

`bug_tracker.py`:

```
# The issue was added to the bug tracker: no longer need the comment
```

`fixed.py`:

```
# The issue was fixed: no longer need the comment
```

`no_fix.py`:

```
# We no longer want to fix this: no longer need the comment
```

**Additional details:**

You can use regular expressions and the `notes-rgx` option to create some constraints for this message.
See [the following issue](https://github.com/pylint-dev/pylint/issues/2874) for some examples.

Created by the [miscellaneous](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/misc.py) checker.