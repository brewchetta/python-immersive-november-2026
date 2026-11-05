"""## **EXERCISE: The Fibonacci Algorithm**

**OBJECTIVE:** Given an integer `N` representing the length of the sequence that we want to generate, output the value from the Fibonacci sequence at the corresponding position of `N`.

**FIBONACCI SEQUENCE**:

- `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...`

**INPUT**: `fibonacci_of(N=10)`

**OUTPUT:** `34`

---
"""

def fibonacci_of(n):
    # if we don't need to iterate
    if n <= 1:
        return 0

    if n == 2:
        return 1

    # set the previous value variables
    prev_2_num = 0
    prev_1_num = 1

    # loop and find the next value, replace prev_2 and prev_1
    for num in range(n - 2):
        next_num = prev_2_num + prev_1_num
        prev_2_num = prev_1_num
        prev_1_num = next_num

    # return the final result
    return prev_1_num


# RECURSIVE SOLUTION #################################################################

values = {
    1: 0,
    2: 1
}

def recursive_fib(n):
    # if we have the value in values use it
    if values.get(n) != None:
        return values[n]
    # otherwise calculate the value using recursion and add it to values
    else:
        new_value = recursive_fib(n - 1) + recursive_fib(n - 2)
        values[n] = new_value
        return new_value