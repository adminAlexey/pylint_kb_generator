---
id: pylint-C0207
rule_code: "C0207"
rule_name: "use-maxsplit-arg"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/use-maxsplit-arg.html"
---
# use-maxsplit-arg / C0207

**Message emitted:**

`Use %s instead`

**Description:**

*Emitted when accessing only the first or last element of str.split(). The first and last element can be accessed by using str.split(sep, maxsplit=1)[0] or str.rsplit(sep, maxsplit=1)[-1] instead.*

**Problematic code:**

```
url = "www.example.com"
suffix = url.split(".")[-1]  # [use-maxsplit-arg]
```

**Correct code:**

```
url = "www.example.com"
suffix = url.rsplit(".", maxsplit=1)[-1]
```

**Additional details:**

Be aware that the performance improvement from not splitting the string
so many times will only be realized in cases presenting more instances of
the splitting character than the minimal example here.

Created by the [refactoring](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/refactoring/recommendation_checker.py) checker.