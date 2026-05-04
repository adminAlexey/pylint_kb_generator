---
id: pylint-I0011
rule_code: "I0011"
rule_name: "locally-disabled"
category: "pylint"
tags: ["python"]
related: []
source: "https://pylint.readthedocs.io/en/latest/user_guide/messages/messages_overview.html"
link: "https://pylint.readthedocs.io/en/latest/user_guide/messages/information/locally-disabled.html"
---
# locally-disabled / I0011

**Message emitted:**

`Locally disabling %s (%s)`

**Description:**

*Used when an inline option disables a message or a messages category.*

Caution

This message is disabled by default. To enable it, add `locally-disabled` to the `enable` option.

Caution

By default, this message will not fail the execution (pylint will return 0).
To make pylint fail for this message use the `--fail-on=I0011` option
or `--fail-on=I` to fail on all enabled informational messages.

**Problematic code:**

```
def wizard_spells(spell_book):
    # pylint: disable=maybe-no-member # [locally-disabled]
    for spell in spell_book:
        print(f"Abracadabra! {spell}.")

spell_list = ["Levitation", "Invisibility", "Fireball", "Teleportation"]
wizard_spells(spell_list)
```

**Correct code:**

```
def wizard_spells(spell_book):
    for spell in spell_book:
        print(f"Abracadabra! {spell}.")

spell_list = ["Levitation", "Invisibility", "Fireball", "Teleportation"]
wizard_spells(spell_list)
```

Created by the [main](https://github.com/pylint-dev/pylint/blob/main/pylint/lint/pylinter.py) checker.