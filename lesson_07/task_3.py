# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. 

# For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

from math import prod


def main():
    """Runs the calculator"""
    OPERATORS = ['+', '-', '*']
    print('\nWelcome to a simple calculator. To perform calculation first enter the operator and next - numbers you want to perform calculation on')
    print('For example: operator: + ; numbers: 10, 20')
    flag = True
    while flag:
        print()
        operator = input('Enter operator here: ')
        print()
        if operator not in OPERATORS:
            print('Please enter valid operator! One of these -> (+, -, *)')
            continue
        numbers_str = input('Enter numbers separated by comma and one space: ').split(', ')
        print()
        if not check_numbers(numbers_str):
            print('Please enter digits only and don\'t forget to use comma with space')
            continue
        numbers = [int(x) for x in numbers_str]
        flag = False
    result = calculator(operator, *numbers)
    print('Your answer is:', result)


def check_numbers(nums: list) -> bool:
    """Returns whether the nums are all digits"""
    for num in nums:
        try:
            int(num)
        except ValueError:
            return False
    return True


def calculator(operator: str, *nums: int) -> int:
    """Return the sum, difference or product of all the numbers"""
    if operator == '+':
        return sum(nums)
    elif operator == '*':
        return prod(nums)
    elif operator == '-':
        diff = None
        for num in nums:
            if diff is None:
                diff = num
            else:
                diff -= num
        return diff


if __name__ == '__main__':
    main()
