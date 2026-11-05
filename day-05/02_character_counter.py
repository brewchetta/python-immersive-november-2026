# WORK UNTIL 11:05 EST
"""
## **EXERCISE: Character Counter**

**OBJECTIVE:** Given a string (e.g. `"hello world"`), we want to design a function/script that can count the frequency of unique characters in that string.

**INPUT:** `character_counter("data")`, `character_counter("DATA")`, `character_counter("Data")`

**OUTPUT:**
  - `"d": 1`
  - `"a": 2`
  - `"t": 1`
---
"""

import re

def character_counter( text ):
    characters = {}

    for letter in text.lower():
      # BONUS: some special regex to only get alphabetical characters
      if not re.match(r'^[a-z]$', letter):
        pass
      elif letter not in characters:
        characters[letter] = 1
      elif letter in characters:
        characters[letter] += 1

    return characters