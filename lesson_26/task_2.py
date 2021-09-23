"""
Task 2

Write a program that reads in a sequence of characters, and determines 
whether it's parentheses, braces, and curly brackets are "balanced."
"""

from typing import Iterable


def main():
    sequence = input()
    print('sequence of chars:', sequence, sep='\n')
    if not is_balanced(sequence):
        print('not balanced')
    else:
        print('balanced')


def is_balanced(sequence: Iterable) -> bool:
    """Returns True if sequence of brackets is balanced"""
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    brackets = opening_brackets + closing_brackets

    if len(sequence) < 2:
        return False

    stack = Stack()
    for char in sequence:
        if char not in brackets:
            continue

        if char in opening_brackets:
            stack.push(char)
        else:
            if stack.is_empty():
                return False

            last_opening = stack.pop()
            if not correspond(last_opening, char):
                return False

    return True


def correspond(bracket_1: str, bracket_2: str) -> bool:
    """Returns True if the brackets are of the same kind"""
    if bracket_1 == '(' and bracket_2 == ')':
        return True

    if bracket_1 == '[' and bracket_2 == ']':
        return True

    if bracket_1 == '{' and bracket_2 == '}':
        return True

    return False


class Stack:

    def __init__(self) -> None:
        self._stack = []
    
    def __repr__(self) -> str:
        return f'{" ".join(self._stack)}'

    def push(self, element) -> None:
        self._stack.append(element)
    
    def pop(self):
        return self._stack.pop()
    
    def is_empty(self) -> bool:
        return bool(not self._stack)
    

if __name__ == '__main__':
    main()