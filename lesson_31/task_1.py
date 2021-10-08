"""
Task 1

Implement a binary heap as a max heap.
"""

from typing import List


class BinHeap:

    def __init__(self) -> None:
        self._heap: List[int] = []
        self._size = len(self._heap)
    
    def parent(self, i) -> int:
        if i == 0:
            return 0
        return (i - 1) // 2

    def left(self, i) -> int:
        l = i * 2 + 1
        return l if l < self._size else i

    def right(self, i) -> int:
        r = i * 2 + 2
        return r if r < self._size else i

    def is_leaf(self, i):
        if i >= (self._size//2) and i < self._size:
            return True
        return False

    def swap(self, i, j) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def heap_up(self, i) -> None:
        if self.is_leaf(i):
            return

        left = self.left(i)
        right = self.right(i)

        if self._heap[i] < self._heap[left] \
            or self._heap[i] < self._heap[right]:

            if self._heap[left] > self._heap[right]:
                self.swap(i, left)
                self.heap_up(left)

            else:
                self.swap(i, right)
                self.heap_up(right)

    def insert(self, element) -> None:
        self._size += 1
        self._heap.append(element)
  
        current = self._size - 1
        while (self._heap[current] > 
            self._heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def get_max_val(self) -> int:
        max_val = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heap.pop()
        self.heap_up(0)
        return max_val
    
    def build_heap(self, array: List[int]) -> None:
        self._heap = array[:]
        self._size = len(array)
        i = self._size // 2 - 1
        while i >= 0:
            self.heap_up(i)
            i -= 1


if __name__ == '__main__':
    array = [2, 3, 5, 6]
    heap = BinHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    print('heap:',heap._heap)

    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    print('heap:',heap._heap)
    print('root:', heap.get_max_val())
    print('heap:',heap._heap)
    print()

    new_heap = BinHeap()
    array_2 = [5, 12, 64, 73, 13, 2, 96]
    new_heap.build_heap(array_2)
    print('new_heap:', new_heap._heap)
    print('root:', new_heap.get_max_val())
    print('new_heap:', new_heap._heap)