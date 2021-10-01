"""
Task 3

One way to improve the quicksort is to use an insertion sort on lists 
that are small in length (call it the “partition limit”). Why does this make sense? 
Re-implement the quicksort and use it to sort a random list of integers. 
Perform analysis using different list sizes for the partition limit.
"""

from typing import List, Optional
from random import shuffle
from sys import setrecursionlimit


def sort_func(array: List[int]):
    if len(array) <= 100_000:
        return insertion_sort_recursive(array)
    
    else:
        return quicksort(array)


def insertion_sort_recursive(array: List[int], i: Optional[int] = None):
    if i is None: i = len(array) - 1
    if i > 0:
        insertion_sort_recursive(array, i - 1)
        insert_last_recursive(array, i)
    return array

def insert_last_recursive(array: List[int], i: int):
    if i > 0 and array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]
        insert_last_recursive(array, i - 1)


def quicksort(array: List[int]): 
    if len(array) < 2:
        return array 
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater) 


if __name__ == '__main__':
    setrecursionlimit(15000)
    print()
    array = list(range(1, 10_000))
    shuffle(array)
    print('Unsorted array:', *array[:50], sep=' ')
    print('Using insertion sort...')
    print('Sorted array:', *sort_func(array)[:50], sep=' ')
    print()

    array = list(range(1, 1_000_000))
    shuffle(array)
    print('Unsorted array:', *array[:50], sep=' ')
    print('Using quicksort...')
    print('Sorted array:', *sort_func(array)[:50], sep=' ')
