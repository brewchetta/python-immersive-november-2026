"""
## **EXERCISE: Fizz(y) Buzz(y)**

**OBJECTIVE:** Given a positive number, print each integer up to that number substituting "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "Fizz Buzz" for numbers divisible by both.

**NOTE:** You are not returning anything with this function, rather you are printing a sequence.

**INPUT:** `fizz_buzz(15)`

**OUTPUT:**
  - `1`
  - `2`
  - `"Fizz"`
  - `4`
  - `"Buzz"`
  - `"Fizz"`
  - `7`
  - `8`
  - `"Fizz"`
  - `"Buzz"`
  - `11`
  - `"Fizz"`
  - `13`
  - `14`
  - `"Fizz Buzz"`

---
"""

def fizz_buzz( integer ):
    for n in range(1, integer + 1):
      if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
      elif n % 3 == 0:
        print("Fizz")
      elif n % 5 == 0:
        print("Buzz")
      else:
        print(n)