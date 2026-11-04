"""###EXERCISE: Human Class

A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `False`.

A `Human` instance has a `workout()` method which sets their attributes `is_hungry` equal to `True`.

A `Human` instance has a `win_lottery()` method which sets their attribute `address` equal to `"Disneyworld"`.

A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>> "`. When a user completes the input the `first_name` attribute changes to their input.

---
"""

class Human:

	# Create a new class `Human` which has required attributes `first_name:str`, `last_name:str`, `address:str`, `age:int`, and `is_hungry:bool`.
	
	def __init__(self, first_name, last_name, address, age, is_hungry):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.age = age
		self.is_hungry = is_hungry

	# A `Human` instance has a `__repr__` that shows their attributes.

	def __repr__(self):
		return f"Human(first_name={self.first_name}, address={self.address}, is_hungry={self.is_hungry})"

	# A `Human` instance has a `full_name()` method which returns their `first_name` and `last_name` in a single string, for example `"Bob Dylan"`.

	def full_name(self):
		return self.first_name + " " + self.last_name
		return f"{self.first_name} {self.last_name}"

	# A `Human` instance has an `order_drinks()` method which either returns `"Party time!"` if their age is 21 or older and returns `"Denied"` if their age is 20 or younger.

	def order_drinks(self):
		if self.age >= 21:
			return "Party time!"
		else:
			return "Denied"

	# A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `False`.

	def eat(self):
		self.is_hungry = False

	# A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>> "`. When a user completes the input the `first_name` attribute changes to their input.

	def change_first_name(self):
		self.first_name = input("Change Name >>> ")