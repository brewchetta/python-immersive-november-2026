# https://github.com/brewchetta/python-immersive-november-2026/blob/main/day-05/01_bill_calculator.py
# WORK UNTIL 10:30am EST
"""
## **EXERCISE: Bill Calculator**

**PROBLEM STATEMENT:**

Let's imagine we're going out to eat at a restaurant; we just had a good meal and we want to calculate the bill. In essence, let's conceptualize and create a custom bill calculator in Python.

**OBJECTIVE:** Given a starting meal price (as a `float`) and a tip quantity (as an `int`) as well as a constant tax rate (as a `float`), calculate the total bill on purchased food.

**INPUT:** `calculate_bill(price_of_food=20.99, amount_tipped=5)`

**OUTPUT:** `27.826625`

**NOTE:** The tax rate and whether the tip is taxed is up to you!

---
"""

price_of_food = 20.99

def calculate_bill(price_of_food, tip_rate=0.20, split=1):
    tip_amount = price_of_food * tip_rate
    tax_amount = price_of_food * 0.0875
    return (price_of_food + tip_amount + tax_amount) / split