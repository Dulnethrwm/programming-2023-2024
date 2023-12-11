# Functions and Recursion
# Author: Dulneth
# Date: 7 December 2023

def factorial(n: int) -> int:
    """Return the nth factorial.
    Done recursively.
    
    Example:
        factorial(3) -> 3! -> 6
        """
    if  n == 0 or n == 1:
        return 1
    elif n > 1:
        return factorial(n - 1) * n
    

def fib(n: int) -> int:
    """Return with nth Fibbinacci number
    Calculated literary"""
    last_num = 0
    num = 1
    result = 1

    for i in range(n):
        result = num + last_num

        num, last_num = result, num

    return result
