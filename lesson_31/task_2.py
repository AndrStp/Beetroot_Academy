"""
Task 2

Using the BinaryHeap class, implement a new class called PriorityQueue.
Your PriorityQueue class should implement the constructor, 
plus the enqueue and dequeue methods.
"""
from task_1 import BinHeap


class PriorityQueue(BinHeap):
    def __init__(self) -> None:
        super().__init__()
    
    def enqueue(self, item) -> None:
        BinHeap.insert(self, item)
    
    def dequeue(self) -> int:
        return BinHeap.get_max_val(self)
    

if __name__ == '__main__':
    prq = PriorityQueue()
    prq.enqueue(10)
    prq.enqueue(20)
    prq.enqueue(30)
    prq.enqueue(50)
    prq.enqueue(40)
    print(prq.dequeue())  # -> 50
    print(prq.dequeue())  # -> 40