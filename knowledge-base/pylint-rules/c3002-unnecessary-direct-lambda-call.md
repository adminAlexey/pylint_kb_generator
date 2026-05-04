---
id: pylint-C3002
rule_code: "C3002"
rule_name: "unnecessary-direct-lambda-call"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/unnecessary-direct-lambda-call.html"
---
# unnecessary-direct-lambda-call / C3002

**Message emitted:**

`Lambda expression called directly. Execute the expression inline instead.`

**Description:**

*Used when a lambda expression is directly called rather than executing its contents inline.*

**Problematic code:**

```
y = (lambda x: x**2 + 2 * x + 1)(a)  # [unnecessary-direct-lambda-call]
```

**Correct code:**

```
y = a**2 + 2 * a + 1
```

Created by the [lambda-expressions](https://github.com/pylint-dev/pylint/blob/main/pylint/checkers/lambda_expressions.py) checker.