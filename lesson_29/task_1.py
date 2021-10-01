"""
Task 1

A bubble sort can be modified to “bubble” in both directions. 
The first pass moves “up” the list and the second pass moves “down.” 
This alternating pattern continues until no more passes are necessary. 
Implement this variation and describe under what circumstances it might be appropriate.
"""

from typing import List


def bottom_bubble_sort(seq: List[int]) -> None:
    """Sorts the List of integers by pushing the lowest item to the beggining"""
    right_end, left_end = len(seq) - 1, 0
    for i in range(right_end):
        for j in range(right_end, left_end + i, -1):
            if seq[j] < seq[j - 1]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]


if __name__ == '__main__':
    l = list(range(4, -1, -1))
    print('unsorted list', l)
    bottom_bubble_sort(l)
    print('sorted list', l)

