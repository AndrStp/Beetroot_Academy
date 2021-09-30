"""
Task 3

Implement a queue using a singly linked list.
"""

from node import Node
from task_1 import UnorderedList


class Queue(UnorderedList):
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, item) -> None:
        UnorderedList.add(self, item)
    
    def dequeue(self) -> None:
        UnorderedList.pop(self)
    
    def size(self) -> int:
        return UnorderedList.get_size(self)
    
    def __repr__(self) -> str:
        representation = 'Queue:\nStart->'
        current = self._head
        while current is not None:
            representation += f"{current.get_data()}->"
            current = current.get_next()
        representation += 'End'
        return representation


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print('queue size:', queue.size(), '\n')
    queue.dequeue()
    print(queue)
    print('queue size:', queue.size())
