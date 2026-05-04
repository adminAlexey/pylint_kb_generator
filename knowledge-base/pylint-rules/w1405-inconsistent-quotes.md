---
id: pylint-W1405
rule_code: "W1405"
rule_name: "inconsistent-quotes"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/inconsistent-quotes.html"
---
# inconsistent-quotes / W1405

**Message emitted:**

`Quote delimiter %s is inconsistent with the rest of the file`

**Description:**

*Quote delimiters are not used consistently throughout a module (with allowances made for avoiding unnecessary escaping).*

**Problematic code:**

```
import datetime

print('Current year: ', datetime.date.today().strftime("%Y")) # [inconsistent-quotes]
```

**Correct code:**

```
import datetime

print("Current year: ", datetime.date.today().strftime("%Y"))
```

**Configuration file:**

```
[main]
check-quote-consistency=yes
```

Created by the [string](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/strings.py) checker.