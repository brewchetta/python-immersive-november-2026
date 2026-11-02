# https://github.com/brewchetta/python-immersive-november-2026/blob/main/day-01/exercises.py
# EXERCISES ##################################################################################

# run exercises with `python -i exercises.py`

# 1. Build the function `say_my_name()` which accepts a `first_name` and a `last_name`
#   The function returns the name as a single full name
#   Example: say_my_name("Chett", "Tiller") --> "Chett Tiller"

def say_my_name(first_name, last_name):
    return f"{first_name} {last_name}"
    return first_name + " " + last_name

# 2. Build the function `is_a_string()` which accepts a single argument `arg`
#   The function returns either "STRING" if `arg` is of type `str` or else "NOT STRING"
# Example: is_a_string("hello") --> "STRING"
# Example: is_a_string(07734) --> "NOT STRING"

def is_a_string(arg):
    if type(arg) == str:
        return "STRING"
    else:
        return "NOT STRING"

# 3. Build the function `stoplight()` which accepts a single argument `color`
#   The function returns "GO" if `color` is "green", "SLOW" for "yellow" and "STOP" for "red"
#   If `color` is none of those three, return "OH NO"
# Example: stoplight("green") --> "GO"
# Example: stoplight("red") --> "STOP"
# Example: stoplight("aquamarine") --> "OH NO"

def stoplight(color):
    if color == "green":
        return "GO"
    elif color == "yellow":
        return "SLOW"
    elif color == "red":
        return "STOP"
    else:
        return "OH NO"

# 4. Build the function `fizz_buzz()` which accepts a single argument `number`
#   The function returns "fizz" if `number` is divisible by 3, "buzz" if divisible by 5
#   Return "fizzbuzz" if divisible by both and just the number if divisible by neither
# Example: fizz_buzz(6) --> "fizz"
# Example: fizz_buzz(10) --> "buzz"
# Example: fizz_buzz(30) --> "fizzbuzz"
# Example: fizz_buzz(31) --> 31

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return number

# 5. Build the function `average()` which accepts two arguments `num1` and `num2`
#   The function return the average of the two numbers
#   Average is calculated as the sum divided by the total number of numbers
# Example: average(10, 20) --> 15
# Example: average(-10, 10) --> 0

def average(num1, num2):
    return (num1 + num2) / 2