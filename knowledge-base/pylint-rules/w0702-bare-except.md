---
id: pylint-W0702
rule_code: "W0702"
rule_name: "bare-except"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bare-except.html"
---
# bare-except / W0702

**Message emitted:**

`No exception type(s) specified`

**Description:**

*A bare ``except:`` clause will catch ``SystemExit`` and ``KeyboardInterrupt`` exceptions, making it harder to interrupt a program with ``Control-C``, and can disguise other problems. If you want to catch all exceptions that signal program errors, use ``except Exception:`` (bare except is equivalent to ``except BaseException:``).*

**Problematic code:**

```
try:
    import platform_specific_module
except:  # [bare-except]
    platform_specific_module = None
```

**Correct code:**

```
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
```

**Additional details:**

A good rule of thumb is to limit use of bare ‘except’ clauses to two cases:
- If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred.
- If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. `try...finally` can be a better way to handle this case.

**Related links:**

- [Programming recommendation in PEP8](https://peps.python.org/pep-0008/#programming-recommendations)
- [PEP 760 – No More Bare Excepts (Rejected)](https://peps.python.org/pep-0760/)
- [Discussion about PEP 760](https://discuss.python.org/t/pep-760-no-more-bare-excepts/67182)

Created by the [exceptions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/exceptions.py) checker.