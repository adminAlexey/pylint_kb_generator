---
id: pylint-E0013
rule_code: "E0013"
rule_name: "bad-plugin-value"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/bad-plugin-value.html"
---
# bad-plugin-value / E0013

**Message emitted:**

`Plugin '%s' is impossible to load, is it installed ? ('%s')`

**Description:**

*Used when a bad value is used in 'load-plugins'.*

**Additional details:**

One of your pylint plugins cannot be loaded. There's nothing to change in
your code, but your pylint configuration or installation has an issue.

For example, there might be a typo. The following config:

```
[MAIN]
load-plugins = pylint.extensions.bad_biultin
```

Should be:

```
[MAIN]
load-plugins = pylint.extensions.bad_builtin
```

Or the plugin you added is not importable in your environment.

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.