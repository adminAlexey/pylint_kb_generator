---
id: pylint-I1101
rule_code: "I1101"
rule_name: "c-extension-no-member"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/c-extension-no-member.html"
---
# c-extension-no-member / I1101

**Message emitted:**

`%s %r has no %r member%s, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects.`

**Description:**

*Used when a variable is accessed for non-existent member of C extension. Due to unavailability of source static analysis is impossible, but it may be performed by introspecting living objects in run-time.*

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I1101` option
or `--fail-on=I` to fail on all enabled informational messages.

**Additional details:**

`c-extension-no-member` is an informational variant of `no-member` to encourage
allowing introspection of C extensions as described in the
[page](https://pylint.readthedocs.io/en/latest/user_guide/messages/error/no-member.html)
for `no-member`.

Created by the [typecheck](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/typecheck.py) checker.