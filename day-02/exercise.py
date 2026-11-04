# =============================================================================
# PYTHON BEGINNER EXERCISES
# =============================================================================
# These are your very first exercises with lists, dictionaries, and loops.
# Each function should RETURN its result (not print it).
# Replace `pass` with your own code.
# =============================================================================
 
 
# 1. Build the function `first_item()` which accepts a single argument `items` (a list of strings)
#   The function returns the first item in the list
#   You may assume the list always has at least one item
# Example: first_item(["red", "green", "blue"]) --> "red"
# Example: first_item(["dog"]) --> "dog"
 
def first_item(items):
    pass
 
 
# 2. Build the function `add_item()` which accepts two arguments: `items` (a list of strings) and `new_item` (a string)
#   The function adds `new_item` to the end of the list and returns the updated list
# Example: add_item(["apple", "banana"], "cherry") --> ["apple", "banana", "cherry"]
# Example: add_item([], "milk") --> ["milk"]
 
def add_item(items, new_item):
    pass
 
 
# 3. Build the function `get_age()` which accepts two arguments: `ages` (a dictionary mapping names (str) to ages (int)) and `name` (a string)
#   The function returns the age stored in the dictionary for `name`
#   You may assume `name` is always in the dictionary
# Example: get_age({"Sam": 12, "Priya": 14}, "Priya") --> 14
# Example: get_age({"Leo": 9}, "Leo") --> 9
 
def get_age(ages, name):
    pass
 
 
# 4. Build the function `add_pet()` which accepts three arguments: `pets` (a dictionary mapping owner names (str) to pet types (str)), `owner` (a string) and `animal` (a string)
#   The function adds `owner` to the dictionary with `animal` as their value, and returns the updated dictionary
# Example: add_pet({"Ana": "cat"}, "Ben", "dog") --> {"Ana": "cat", "Ben": "dog"}
# Example: add_pet({}, "Cy", "fish") --> {"Cy": "fish"}
 
def add_pet(pets, owner, animal):
    pass
 
 
# 5. Build the function `total()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to add up every number in the list and returns the sum
#   If the list is empty, return 0
# Example: total([1, 2, 3, 4]) --> 10
# Example: total([]) --> 0
 
def total(numbers):
    pass
 
 
# 6. Build the function `double_all()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to build a new list where every number has been multiplied by 2, and returns the new list
# Example: double_all([1, 2, 3]) --> [2, 4, 6]
# Example: double_all([5]) --> [10]
 
numbers = [1,2,3,4,5,0,-5]

def double_all(numbers):
    new_list = []
    for n in numbers:
        doubled = n * 2
        new_list.append(doubled)
    return new_list
    # alternative
    return [ num * 2 for num in numbers ]
 
 
# 7. Build the function `countdown()` which accepts a single argument `start` (a positive integer)
#   The function uses a while loop to build a list that counts down from `start` to 1, and returns the list
# Example: countdown(3) --> [3, 2, 1]
# Example: countdown(1) --> [1]
 
def countdown(start):
    pass
 
 
# 8. Build the function `describe_number()` which accepts a single argument `number` (an integer)
#   The function returns "positive" if `number` is greater than 0 and "negative" if it is less than 0
#   If `number` is 0, return "zero"
# Example: describe_number(8) --> "positive"
# Example: describe_number(-3) --> "negative"
 
def describe_number(number):
    pass
 
 
# 9. Build the function `add_text_numbers()` which accepts two arguments: `first` (a string) and `second` (a string)
#   Both strings are whole numbers written as text, such as "5"
#   The function converts both to integers and returns their sum as an integer
# Example: add_text_numbers("5", "7") --> 12
# Example: add_text_numbers("10", "20") --> 30
 
def add_text_numbers(first, second):
    pass
 
 
# 10. Build the function `count_big()` which accepts a single argument `numbers` (a list of integers)
#   The function uses a for loop to count how many numbers in the list are greater than 10, and returns that count
# Example: count_big([4, 12, 30, 7]) --> 2
# Example: count_big([1, 2, 3]) --> 0
 
def count_big(numbers):
    pass


# BONUS QUESTIONS -------------------------------------------------------------


# B1. Build the function `sum_of_evens()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the sum of only the even numbers in the list
#   If there are no even numbers, return 0
# Example: sum_of_evens([1, 2, 3, 4, 5, 6]) --> 12
# Example: sum_of_evens([7, 9, 11]) --> 0
 
def sum_of_evens(numbers):
    pass
 
 
# B2. Build the function `word_frequency()` which accepts a single argument `words` (a list of strings)
#   The function returns a dictionary mapping each word to the number of times it appears in the list
# Example: word_frequency(["apple", "banana", "apple"]) --> {"apple": 2, "banana": 1}
# Example: word_frequency([]) --> {}
 
def word_frequency(words):
    pass
 
 
# B3. Build the function `count_digits()` which accepts a single argument `number` (a non-negative integer)
#   The function returns how many digits are in `number`
#   You must use a while loop (do not convert the number to a string)
# Example: count_digits(12345) --> 5
# Example: count_digits(0) --> 1
 
def count_digits(number):
    pass
 
 
# B4. Build the function `fizzbuzz_list()` which accepts a single argument `n` (a positive integer)
#   The function returns a list of strings, one for each number from 1 through `n`
#   Multiples of 3 become "Fizz", multiples of 5 become "Buzz", and multiples of both become "FizzBuzz"
#   All other numbers become the number as a string
# Example: fizzbuzz_list(5) --> ["1", "2", "Fizz", "4", "Buzz"]
# Example: fizzbuzz_list(3) --> ["1", "2", "Fizz"]
 
def fizzbuzz_list(n):
    pass
 
 
# B5. Build the function `count_types()` which accepts a single argument `values` (a list containing values of mixed types)
#   The function returns a dictionary mapping each type's name to how many values of that type are in the list
#   Hint: `type(value).__name__` gives the name of a value's type as a string
# Example: count_types([1, "a", 2.5, True, "b"]) --> {"int": 1, "str": 2, "float": 1, "bool": 1}
# Example: count_types([3, 4, 5]) --> {"int": 3}
 
def count_types(values):
    pass
 
 
# B6. Build the function `items_within_budget()` which accepts two arguments: `prices` (a list of floats) and `budget` (a float)
#   The function goes through `prices` in order, buying each item as long as the running total stays within `budget`
#   Stop at the first item that would push the total over the budget
#   The function returns the number of items purchased
#   You must use a while loop
# Example: items_within_budget([3.5, 2.0, 4.0, 1.5], 6.0) --> 2
# Example: items_within_budget([5.0, 5.0], 4.0) --> 0
 
def items_within_budget(prices, budget):
    pass
 
 
# B7. Build the function `grade_report()` which accepts a single argument `scores` (a dictionary mapping student names (str) to scores (int))
#   The function returns a dictionary mapping each student name to a letter grade
#   90 and above is "A", 80-89 is "B", 70-79 is "C", 60-69 is "D", and below 60 is "F"
# Example: grade_report({"Ana": 95, "Ben": 72, "Cy": 58}) --> {"Ana": "A", "Ben": "C", "Cy": "F"}
# Example: grade_report({"Dee": 80, "Eli": 89}) --> {"Dee": "B", "Eli": "B"}
 
def grade_report(scores):
    pass
 
 
# B8. Build the function `second_largest()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the second largest DISTINCT value in the list
#   If the list has fewer than two distinct values, return None
# Example: second_largest([4, 9, 2, 7]) --> 7
# Example: second_largest([5, 5]) --> None
 
def second_largest(numbers):
    pass
 
 
# B9. Build the function `collatz_steps()` which accepts a single argument `n` (a positive integer)
#   Repeat the following until `n` equals 1: if `n` is even, divide it by 2; if `n` is odd, multiply it by 3 and add 1
#   The function returns the number of steps it took to reach 1
# Example: collatz_steps(6) --> 8   (6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
# Example: collatz_steps(1) --> 0
 
def collatz_steps(n):
    pass
 
 
# B10. Build the function `invert_dictionary()` which accepts a single argument `data` (a dictionary mapping strings to unique integers)
#   The function returns a new dictionary where each original value is now a key and each original key is now a value
# Example: invert_dictionary({"x": 10, "y": 20, "z": 30}) --> {10: "x", 20: "y", 30: "z"}
# Example: invert_dictionary({}) --> {}
 
def invert_dictionary(data):
    pass
 
 
# B11. Build the function `honor_roll()` which accepts two arguments: `students` (a list of dictionaries) and `min_gpa` (a float)
#   Each dictionary in `students` has a "name" key (a string) and a "gpa" key (a float)
#   The function returns a list of the names of students whose GPA is at least `min_gpa`, in their original order
# Example: honor_roll([{"name": "Ana", "gpa": 3.8}, {"name": "Ben", "gpa": 2.9}], 3.0) --> ["Ana"]
# Example: honor_roll([{"name": "Cy", "gpa": 3.0}, {"name": "Dee", "gpa": 3.2}], 3.0) --> ["Cy", "Dee"]
 
def honor_roll(students, min_gpa):
    pass
 
 
# B12. Build the function `is_palindrome()` which accepts a single argument `text` (a string)
#   The function returns True if `text` reads the same forwards and backwards, ignoring spaces and letter case
#   Otherwise, it returns False
# Example: is_palindrome("Never odd or even") --> True
# Example: is_palindrome("Python") --> False
 
def is_palindrome(text):
    pass
