# -----------------------------------------------------------------------------
# Exercise 1: First Item
# Concepts: lists (indexing)
#
# Write a function `first_item` that returns the first item in a list.
#
# Arguments:
#   - items (list[str]): a list containing at least one string
#
# Returns: str, the first item in the list.
#
# Examples:
#   - Input: ["red", "green", "blue"]  ->  Output: "red"
#   - Input: ["dog"]                   ->  Output: "dog"

# ["dog", "cat", "polar bear"]

def first_item(items):
    return items[0]


# -----------------------------------------------------------------------------
# Exercise 2: Add to the List
# Concepts: lists (adding items)
#
# Write a function `add_item` that adds a new item to the end of a list and
# returns the updated list.
#
# Arguments:
#   - items (list[str]): a list of strings
#   - new_item (str): the string to add to the end of the list
#
# Returns: list[str], the list with the new item added at the end.
#
# Examples:
#   - Input: ["apple", "banana"], "cherry"  ->  Output: ["apple", "banana", "cherry"]
#   - Input: [], "milk"                     ->  Output: ["milk"]


# -----------------------------------------------------------------------------
# Exercise 3: Look Up an Age
# Concepts: dictionaries (looking up a value by key)
#
# Write a function `get_age` that returns the age stored for a given name in
# a dictionary. You may assume the name is always in the dictionary.
#
# Arguments:
#   - ages (dict[str, int]): maps people's names to their ages
#   - name (str): the name to look up
#
# Returns: int, the age belonging to that name.
#
# Examples:
#   - Input: {"Sam": 12, "Priya": 14}, "Priya"  ->  Output: 14
#   - Input: {"Leo": 9}, "Leo"                  ->  Output: 9


# -----------------------------------------------------------------------------
# Exercise 4: Add a Pet
# Concepts: dictionaries (adding a key and value)
#
# Write a function `add_pet` that adds a new person and their pet to a
# dictionary and returns the updated dictionary.
#
# Arguments:
#   - pets (dict[str, str]): maps owners' names to the type of pet they own
#   - owner (str): the name of the new owner
#   - animal (str): the type of pet the new owner has
#
# Returns: dict[str, str], the dictionary with the new owner and pet added.
#
# Examples:
#   - Input: {"Ana": "cat"}, "Ben", "dog"  ->  Output: {"Ana": "cat", "Ben": "dog"}
#   - Input: {}, "Cy", "fish"              ->  Output: {"Cy": "fish"}


# -----------------------------------------------------------------------------
# Exercise 5: Add Up the Numbers
# Concepts: for loops, lists
#
# Write a function `total` that uses a for loop to add up every number in a
# list.
#
# Arguments:
#   - numbers (list[int]): a list of integers
#
# Returns: int, the sum of all the numbers (0 if the list is empty).
#
# Examples:
#   - Input: [1, 2, 3, 4]  ->  Output: 10
#   - Input: []            ->  Output: 0


# -----------------------------------------------------------------------------
# Exercise 6: Double Each Number
# Concepts: for loops, lists
#
# Write a function `double_all` that uses a for loop to build a new list where
# every number from the original list has been multiplied by 2.
#
# Arguments:
#   - numbers (list[int]): a list of integers
#
# Returns: list[int], a new list with each number doubled.
#
# Examples:
#   - Input: [1, 2, 3]  ->  Output: [2, 4, 6]
#   - Input: [5]        ->  Output: [10]


# -----------------------------------------------------------------------------
# Exercise 7: Countdown
# Concepts: while loops, lists
#
# Write a function `countdown` that uses a while loop to build a list that
# counts down from a starting number to 1.
#
# Arguments:
#   - start (int): a positive integer to start counting down from
#
# Returns: list[int], the numbers from start down to 1.
#
# Examples:
#   - Input: 3  ->  Output: [3, 2, 1]
#   - Input: 1  ->  Output: [1]


# -----------------------------------------------------------------------------
# Exercise 8: Positive, Negative, or Zero
# Concepts: conditional logic (if / elif / else)
#
# Write a function `describe_number` that decides whether a number is
# positive, negative, or zero.
#
# Arguments:
#   - number (int): any integer
#
# Returns: str, either "positive", "negative", or "zero".
#
# Examples:
#   - Input: 8   ->  Output: "positive"
#   - Input: -3  ->  Output: "negative"


# -----------------------------------------------------------------------------
# Exercise 9: Add Two Numbers from Text
# Concepts: data types (converting a string to an integer)
#
# Write a function `add_text_numbers` that takes two numbers written as strings,
# converts them to integers, and returns their sum.
#
# Arguments:
#   - first (str): a whole number written as text, such as "5"
#   - second (str): a whole number written as text, such as "7"
#
# Returns: int, the sum of the two numbers.
#
# Examples:
#   - Input: "5", "7"    ->  Output: 12
#   - Input: "10", "20"  ->  Output: 30


# -----------------------------------------------------------------------------
# Exercise 10: Count the Big Numbers
# Concepts: for loops, lists, conditional logic
#
# Write a function `count_big` that uses a for loop to count how many numbers
# in a list are greater than 10.
#
# Arguments:
#   - numbers (list[int]): a list of integers
#
# Returns: int, how many numbers in the list are greater than 10.
#
# Examples:
#   - Input: [4, 12, 30, 7]  ->  Output: 2
#   - Input: [1, 2, 3]       ->  Output: 0


# BONUS QUESTIONS -------------------------------------------------------------


# -----------------------------------------------------------------------------
# Exercise 1: Sum of Evens
# Concepts: lists, for loops, conditionals
#
# Write a function `sum_of_evens` that adds up only the even numbers in a list.
#
# Arguments:
#   - numbers (list[int]): a list of integers
#
# Returns: int, the sum of all even numbers (0 if there are none).
#
# Examples:
#   - Input: [1, 2, 3, 4, 5, 6]  ->  Output: 12
#   - Input: [7, 9, 11]          ->  Output: 0
 
 
 
# -----------------------------------------------------------------------------
# Exercise 2: Word Frequency
# Concepts: dictionaries, for loops
#
# Write a function `word_frequency` that counts how many times each word
# appears in a list.
#
# Arguments:
#   - words (list[str]): a list of words
#
# Returns: dict[str, int], mapping each word to its count.
#
# Examples:
#   - Input: ["apple", "banana", "apple"]  ->  Output: {"apple": 2, "banana": 1}
#   - Input: []                            ->  Output: {}
 
 
 
# -----------------------------------------------------------------------------
# Exercise 3: FizzBuzz List
# Concepts: for loops, conditional logic, lists
#
# Write a function `fizzbuzz_list` that builds a list for the numbers 1
# through `n`. For each number:
#   - Multiples of 3 become "Fizz"
#   - Multiples of 5 become "Buzz"
#   - Multiples of both become "FizzBuzz"
#   - All other numbers become the number as a string
#
# Arguments:
#   - n (int): a positive integer
#
# Returns: list[str], one entry per number from 1 to n.
#
# Examples:
#   - Input: 5  ->  Output: ["1", "2", "Fizz", "4", "Buzz"]
#   - Input: 3  ->  Output: ["1", "2", "Fizz"]
 
 
# -----------------------------------------------------------------------------
# Exercise 4: Budget Shopper
# Concepts: while loops, lists, conditional logic
#
# Write a function `items_within_budget` that goes through item prices IN ORDER,
# buying each one as long as the running total stays within the budget. Stop at
# the first item that would push the total over the budget. Use a while loop.
#
# Arguments:
#   - prices (list[float]): item prices, in the order they are encountered
#   - budget (float): the total amount available to spend
#
# Returns: int, the number of items purchased.
#
# Examples:
#   - Input: [3.5, 2.0, 4.0, 1.5], 6.0  ->  Output: 2
#   - Input: [5.0, 5.0], 4.0            ->  Output: 0
 
 
 
# -----------------------------------------------------------------------------
# Exercise 5: Letter Grades
# Concepts: dictionaries, for loops, conditional logic
#
# Write a function `grade_report` that converts numeric scores to letter grades
# using this scale:
#   - 90+   = "A"
#   - 80-89 = "B"
#   - 70-79 = "C"
#   - 60-69 = "D"
#   - below 60 = "F"
#
# Arguments:
#   - scores (dict[str, int]): maps student names to scores
#
# Returns: dict[str, str], mapping each student name to their letter grade.
#
# Examples:
#   - Input: {"Ana": 95, "Ben": 72, "Cy": 58}
#       ->  Output: {"Ana": "A", "Ben": "C", "Cy": "F"}
#   - Input: {"Dee": 80, "Eli": 89}
#       ->  Output: {"Dee": "B", "Eli": "B"}
 
 
 
# -----------------------------------------------------------------------------
# Exercise 6: Second Largest
# Concepts: lists, for loops, conditional logic
#
# Write a function `second_largest` that finds the second largest DISTINCT
# value in a list. If the list has fewer than two distinct values, return None.
#
# Arguments:
#   - numbers (list[int]): a list of integers
#
# Returns: int or None, the second largest distinct value.
#
# Examples:
#   - Input: [4, 9, 2, 7]  ->  Output: 7
#   - Input: [5, 5]        ->  Output: None
 
 
 
# -----------------------------------------------------------------------------
# Exercise 7: Collatz Steps
# Concepts: while loops, conditional logic, integer arithmetic
#
# Write a function `collatz_steps` that counts how many steps it takes to reach
# 1 using this process, repeated until the number equals 1:
#   - If the number is even, divide it by 2
#   - If the number is odd, multiply it by 3 and add 1
#
# Arguments:
#   - n (int): a positive integer
#
# Returns: int, the number of steps needed to reach 1.
#
# Examples:
#   - Input: 6  ->  Output: 8
#       (6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
#   - Input: 1  ->  Output: 0
 
 
 
# -----------------------------------------------------------------------------
# Exercise 8: Invert a Dictionary
# Concepts: dictionaries, for loops
#
# Write a function `invert_dictionary` that swaps keys and values. You may
# assume all values are unique.
#
# Arguments:
#   - data (dict[str, int]): a dictionary with unique integer values
#
# Returns: dict[int, str], where each original value is now a key and each
# original key is now a value.
#
# Examples:
#   - Input: {"x": 10, "y": 20, "z": 30}
#       ->  Output: {10: "x", 20: "y", 30: "z"}
#   - Input: {}
#       ->  Output: {}
# -----------------------------------------------------------------------------
 
 
 
# -----------------------------------------------------------------------------
# Exercise 9: Honor Roll
# Concepts: lists of dictionaries, for loops, conditional logic
#
# Write a function `honor_roll` that returns the names of students whose GPA is
# AT LEAST the minimum, in their original order.
#
# Arguments:
#   - students (list[dict]): each dictionary has a "name" (str) and a
#                            "gpa" (float)
#   - min_gpa (float): the minimum GPA required
#
# Returns: list[str], the qualifying students' names.
#
# Examples:
#   - Input: [{"name": "Ana", "gpa": 3.8}, {"name": "Ben", "gpa": 2.9}], 3.0
#       ->  Output: ["Ana"]
#   - Input: [{"name": "Cy", "gpa": 3.0}, {"name": "Dee", "gpa": 3.2}], 3.0
#       ->  Output: ["Cy", "Dee"]
# -----------------------------------------------------------------------------
 
 
 
# -----------------------------------------------------------------------------
# Exercise 10: Palindrome Checker
# Concepts: strings, data types, conditional logic, loops
#
# Write a function `is_palindrome` that checks whether a phrase reads the same
# forwards and backwards, ignoring spaces and letter case.
#
# Arguments:
#   - text (str): the phrase to check
#
# Returns: bool, True if it is a palindrome, otherwise False.
#
# Examples:
#   - Input: "Never odd or even"  ->  Output: True
#   - Input: "Python"             ->  Output: False
# -----------------------------------------------------------------------------
