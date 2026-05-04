---
id: pylint-E0601
rule_code: "E0601"
rule_name: "used-before-assignment"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/error/used-before-assignment.html"
---
# used-before-assignment / E0601

**Message emitted:**

`Using variable %r before assignment`

**Description:**

*Emitted when a local variable is accessed before its assignment took place. Assignments in try blocks are assumed not to have occurred when evaluating associated except/finally blocks. Assignments in except blocks are assumed not to have occurred when evaluating statements outside the block, except when the associated try block contains a return statement.*

**Problematic code:**

```
print(hello)  # [used-before-assignment]
hello = "Hello World !"
```

**Correct code:**

```
hello = "Hello World !"
print(hello)
```

Created by the [variables](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/variables.py) checker.