"""
Task 1

Implement binary search using recursion.
"""

from typing import Iterable, Union


def search(seq: Iterable[Union[int, str]], item: Union[int, str]) -> int:
    """Return index of the item if present, otherwise returns -1"""
    def binary_search(sequence, start, stop):
        if stop >= start:
            middle = start + (stop - start) // 2
            if sequence[middle] == item:
                return middle
            
            if sequence[middle] > item:
                return binary_search(sequence, start, middle - 1)
            return binary_search(sequence, middle + 1, stop)
        else:
            return -1

    return binary_search(seq, 0, len(seq) - 1)


if __name__ == '__main__':
    print(search([1, 2, 3], 3))
    print(search([1, 2, 3], 4))
    print(search(list(range(10)), 3))