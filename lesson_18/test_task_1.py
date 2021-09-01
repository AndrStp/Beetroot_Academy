# Pick your solution to one of the exercises in this module. 
# Design tests for this solution and write tests using unittest library.

# test_decorator.py

from decorator import create_slogan


def test_type_create_slogan():
    """Func takes only strings as input"""
    assert create_slogan('johndoe05@gmail.com') is False


def test_len_create_slogan():
    """Max length for the input is 15"""
    assert create_slogan('123456789@coolmail.com') is False


def test_contain_create_slogan():
    """Input should not contain NECESSARY elements"""
    assert create_slogan('john@gmail.com') is False


def test_empty_create_slogan():
    """Input cannot be empty"""
    assert create_slogan('') is False
