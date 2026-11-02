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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 3: Count the Digits
# Concepts: while loops, integer arithmetic
#
# Write a function `count_digits` that counts the digits in a non-negative
# integer USING A WHILE LOOP (do not convert the number to a string).
#
# Arguments:
#   - number (int): a non-negative integer
#
# Returns: int, the number of digits.
#
# Examples:
#   - Input: 12345  ->  Output: 5
#   - Input: 0      ->  Output: 1
# -----------------------------------------------------------------------------
 
 
 
# -----------------------------------------------------------------------------
# Exercise 4: FizzBuzz List
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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 5: Count the Types
# Concepts: data types, dictionaries, for loops
#
# Write a function `count_types` that counts how many values of each data type
# appear in a list. Use the type's name (e.g. type(value).__name__) as the
# dictionary key.
#
# Arguments:
#   - values (list): a list containing values of mixed types
#
# Returns: dict[str, int], mapping each type name to how many times it appears.
#
# Examples:
#   - Input: [1, "a", 2.5, True, "b"]
#       ->  Output: {"int": 1, "str": 2, "float": 1, "bool": 1}
#   - Input: [3, 4, 5]
#       ->  Output: {"int": 3}
# -----------------------------------------------------------------------------
 
 
 
# -----------------------------------------------------------------------------
# Exercise 6: Budget Shopper
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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 7: Letter Grades
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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 8: Second Largest
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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 9: Collatz Steps
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
 
 
 
# -----------------------------------------------------------------------------
# Exercise 10: Invert a Dictionary
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
# Exercise 11: Honor Roll
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
# Exercise 12: Palindrome Checker
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