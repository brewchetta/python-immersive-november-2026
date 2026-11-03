# https://github.com/brewchetta/python-immersive-november-2026/blob/main/day-03/exercises.py

"""###EXERCISE: Human Class

Create a new class `Human` which has required attributes `first_name:str`, `last_name:str`, `address:str`, `age:int`, and `is_hungry:bool`.

A `Human` instance has a `__repr__` that shows their attributes.

A `Human` instance has a `full_name()` method which returns their `first_name` and `last_name` in a single string, for example `"Bob Dylan"`.

A `Human` instance has an `order_drinks()` method which either returns `"Party time!"` if their age is 21 or older and returns `"Denied"` if their age is 20 or younger.

A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `False`.

A `Human` instance has a `workout()` method which sets their attributes `is_hungry` equal to `True`.

A `Human` instance has a `win_lottery()` method which sets their attribute `address` equal to `"Disneyworld"`.

A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>> "`. When a user completes the input the `first_name` attribute changes to their input.

---
"""

class Human:
	pass