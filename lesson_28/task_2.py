"""
Task 2

Read about the Fibonacci search and implement it using python. 
Explore its complexity and compare it to sequential, binary searches.
"""

from typing import List


def fib_search(seq: List[int], item: int) -> int:
    """Return index of the item if present, otherwise returns -1"""
    fib_2, fib_1 = 0, 1 # fib_(n-2) and fib_(n-1)
    fib_n = fib_1 + fib_2 # fib_n

    while fib_n < len(seq):
        fib_2, fib_1, fib_n = fib_1, fib_n, fib_1 + fib_n

    start = -1
    while fib_n > 1:
        index = min(start + fib_2, len(seq) - 1)
        if seq[index] < item:
            fib_n = fib_1
            fib_1 = fib_2
            fib_2 = fib_n - fib_1
            start = index
        elif seq[index] > item:
            fib_n = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_n - fib_1
        else:
            return index
    if fib_1 and (seq[len(seq) - 1] == item):
        return len(seq) - 1
    return -1


if __name__ == '__main__':
    print(fib_search(list(range(0, 100)), 0))
    print(fib_search(list(range(0, 100)), 50))
    print(fib_search(list(range(0, 100)), 100))