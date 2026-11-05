"""
## **EXERCISE: The ROT-13 Algorithm**

**OBJECTIVE:** Given some message (string) to encode, we want to design a function that changes every letter in the string to the letter that is `13` positions forward in the English alphabet.

**INPUT:** `rot_13( "hello there" )`

abcdefghijklmnopqrstuvwxyz
       ^            ^
    original       new

**OUTPUT:** `"uryyb gurer"`

**HINT:** There is a numerical way to "shift" a character X places in ASCII and Unicode. Additionally, if the letter goes past "z" you will need to figure out how to wrap back around from the beginning of the alphabet.

---
"""

def rot_13():
    pass


"""
## **BONUS: The ROT-N Algorithm**

**OBJECTIVE:** Given some message (a string) to encode, construct a class with the ability to apply a ROT substitution transformation to encrypt (or decrypt) the message with degree `N`.

**INPUT:** `rot_n( "hello there", 14 )`

**OUTPUT:** `"vszzc hvsfs"`

---
"""

def rot_n():
    pass