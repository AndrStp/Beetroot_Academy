"""
Task 1

Write a program that reads in a sequence of characters and prints them in 
reverse order, using your implementation of Stack.
"""

from typing import Iterable


def main():
    stck = Stack('abcde')
    print('sequence of chars:', stck, sep='\n')

    print('reversed sequence of chars:')
    if not stck.is_empty():
        for item in stck:
            print(item, end=' ')
        print()


class Stack:

    def __init__(self, sequence: Iterable = None) -> None:
        if not sequence:
            self._stack = []
        else:
            self._stack = list(sequence)
        
        self.__index = 0
        self.__len = len(self._stack)
    
    def __repr__(self) -> str:
        return f'{" ".join(self._stack)}'

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index >= self.__len:
            raise StopIteration
        else:
            self.__index += 1
            return Stack.pop(self)

    def push(self, element) -> None:
        self._stack.append(element)
    
    def pop(self):
        return self._stack.pop()
    
    def is_empty(self) -> bool:
        return bool(not self._stack)
    

if __name__ == '__main__':
    main()