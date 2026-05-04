---
id: pylint-R5601
rule_code: "R5601"
rule_name: "confusing-consecutive-elif"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/confusing-consecutive-elif.html"
---
# confusing-consecutive-elif / R5601

**Message emitted:**

`Consecutive elif with differing indentation level, consider creating a function to separate the inner elif`

**Description:**

*Used when an elif statement follows right after an indented block which itself ends with if or elif. It may not be obvious if the elif statement was willingly or mistakenly unindented. Extracting the indented if statement into a separate function might avoid confusion and prevent errors.*

**Problematic code:**

```
def myfunc(shall_continue: bool, shall_exit: bool):
    if shall_continue:
        if input("Are you sure?") == "y":
            print("Moving on.")
    elif shall_exit:  # [confusing-consecutive-elif]
        print("Exiting.")
```

**Correct code:**

```
# Option 1: add explicit 'else'
def myfunc(shall_continue: bool, shall_exit: bool):
    if shall_continue:
        if input("Are you sure?") == "y":
            print("Moving on.")
        else:
            pass
    elif shall_exit:
        print("Exiting.")

# Option 2: extract function
def user_confirmation():
    if input("Are you sure?") == "y":
        print("Moving on.")

def myfunc2(shall_continue: bool, shall_exit: bool):
    if shall_continue:
        user_confirmation()
    elif shall_exit:
        print("Exiting.")
```

**Configuration file:**

```
[MAIN]
load-plugins=pylint.extensions.confusing_elif
```

**Additional details:**

Creating a function for the nested conditional, or adding an explicit `else` in the indented `if` statement, even if it only contains a `pass` statement, can help clarify the code.

Note

This message is emitted by the optional ['confusing_elif'](https://pylint.readthedocs.io/en/latest/checkers/extensions.html#pylint-extensions-confusing-elif)
checker, which requires the `pylint.extensions.confusing_elif` plugin to be loaded.

Created by the [confusing_elif](https://github.com/pylint-dev/pylint/blob/main/pylint/extensions/confusing_elif.py) checker.