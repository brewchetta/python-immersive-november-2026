# BONUS CHALLENGES #######################

# B1. Build the function `sum_of_evens()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the sum of only the even numbers in the list
#   If there are no even numbers, return 0
# Example: sum_of_evens([1, 2, 3, 4, 5, 6]) --> 12
# Example: sum_of_evens([7, 9, 11]) --> 0
 
def sum_of_evens(numbers):
    pass


# B2. Build the function `items_within_budget()` which accepts two arguments: `prices` (a list of floats) and `budget` (a float)
#   The function goes through `prices` in order, buying each item as long as the running total stays within `budget`
#   Stop at the first item that would push the total over the budget
#   The function returns the number of items purchased
#   You must use a while loop
# Example: items_within_budget([3.5, 2.0, 4.0, 1.5], 6.0) --> 2
# Example: items_within_budget([5.0, 5.0], 4.0) --> 0
 
def items_within_budget(prices, budget):
    pass


# B3. Build the function `grade_report()` which accepts a single argument `scores` (a dictionary mapping student names (str) to scores (int))
#   The function returns a dictionary mapping each student name to a letter grade
#   90 and above is "A", 80-89 is "B", 70-79 is "C", 60-69 is "D", and below 60 is "F"
# Example: grade_report({"Ana": 95, "Ben": 72, "Cy": 58}) --> {"Ana": "A", "Ben": "C", "Cy": "F"}
# Example: grade_report({"Dee": 80, "Eli": 89}) --> {"Dee": "B", "Eli": "B"}
 
def grade_report(scores):
    pass


# B4. Build the function `is_palindrome()` which accepts a single argument `text` (a string)
#   The function returns True if `text` reads the same forwards and backwards, ignoring spaces and letter case
#   Otherwise, it returns False
# Example: is_palindrome("Never odd or even") --> True
# Example: is_palindrome("Python") --> False
 
def is_palindrome(text):
    pass


# B5. Build the function `second_largest()` which accepts a single argument `numbers` (a list of integers)
#   The function returns the second largest DISTINCT value in the list
#   If the list has fewer than two distinct values, return None
# Example: second_largest([4, 9, 2, 7]) --> 7
# Example: second_largest([5, 5]) --> None
 
def second_largest(numbers):
    pass