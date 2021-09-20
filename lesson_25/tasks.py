"""
#############################################
# All tasks should be solved using recursion
#############################################
"""

from typing import Union


# Task 1
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """Returns  x ^ exp"""
    if exp < 0:
        raise ValueError('ValueError: This function works only with exp > 0.')

    if exp == 0:
        return 1
    return x * to_power(x, exp-1)


# Task 2
def is_palindrome(looking_str: str) -> bool:
    """Returns True if the given word is palindrome"""
    if isinstance(looking_str, int):
        raise ValueError('ValueError: Only strings accepted')

    if len(looking_str) < 2:
        return True

    looking_str = looking_str.lower()
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


# Task 3
def mult(a: int, n: int) -> int:
    """Return the result of a * n"""
    if n < 0:
        raise ValueError("This function works only with postive integers")

    if not isinstance(a, int) or not isinstance(n, int):
        raise TypeError("Accepts only integers")
        
    if n < 1:
        return 0
    return a + mult(a, n-1)


# Task 4
def reverse(input_str: str) -> str:
    """Return a reversed string"""
    if len(input_str) == 0:
        return input_str
    return reverse(input_str[1:]) + input_str[0]


# Task 5
def sum_of_digits(digit_string: str) -> int:
    """Return the sum of digits in the given string"""
    if not digit_string.isdigit():
        raise ValueError("Input string must be digit string")
    
    if len(digit_string) == 1:
        return int(digit_string[0])
    return int(digit_string[-1]) + sum_of_digits(digit_string[:-1])