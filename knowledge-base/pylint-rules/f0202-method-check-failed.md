---
id: pylint-F0202
rule_code: "F0202"
rule_name: "method-check-failed"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/fatal/method-check-failed.html"
---
# method-check-failed / F0202

**Message emitted:**

`Unable to check methods signature (%s / %s)`

**Description:**

*Used when Pylint has been unable to check methods signature compatibility for an unexpected reason. Please report this kind if you don't make sense of it.*

**Additional details:**

This is a message linked to an internal problem in pylint. There's nothing to change in your code.

Created by the [classes](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/classes/class_checker.py) checker.