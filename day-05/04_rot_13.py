"""
## **EXERCISE: The ROT-13 Algorithm**

**OBJECTIVE:** Given some message (string) to encode, we want to design a function that changes every letter in the string to the letter that is `13` positions forward in the English alphabet.

**INPUT:** `rot_13( "hello there" )`

abcdefghijklmnopqrstuvwxyz
       ^            ^
    original       new

**OUTPUT:** `"uryyb gurer"`

**HINT:** There is a numerical way to "shift" a character X places in ASCII and Unicode. Additionally, if the letter goes past "z" you will need to figure out how to wrap back around from the beginning of the alphabet.

**NOTE:** You may choose to lowercase letters before converting them since capitalizations add extra work.

---
"""

def rot_13( string ):
    new_string = ""
    for l in string.lower():
        # if front half of alphabet
        if 97 <= ord(l) <= 109:
            new_code = ord(l) + 13
            new_string += chr(new_code)
        # if back half of alphabet
        elif 110 <= ord(l) <= 122:
            new_code = ord(l) - 13
            new_string += chr(new_code)
        # if not in alphabet
        else:
            new_string += l
    return new_string

"""
## **BONUS: The ROT-N Algorithm**

**OBJECTIVE:** Given some message (a string) to encode, construct a class with the ability to apply a ROT substitution transformation to encrypt (or decrypt) the message with degree `N`.

**INPUT:** `rot_n( "hello there", 14 )`

**OUTPUT:** `"vszzc hvsfs"`

---
"""

def rot_n():
    pass