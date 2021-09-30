"""
Task 2

Implement a stack using a singly linked list.
"""

from node import Node
from task_1 import UnorderedList


class Stack(UnorderedList):
    def __init__(self):
        super().__init__()
    
    def push(self, item):
        UnorderedList.append(self, item)
    
    def pop(self):
        return UnorderedList.pop(self)

    def size(self):
        return UnorderedList.get_size(self)
    
    def __repr__(self):
        representation = "Stack:\n"
        elements = []
        current = self._head
        while current is not None:
            elements.append(f'({current.get_data()})\n')
            current = current.get_next()
        for i in range(len(elements)-1, -1, -1):
            representation += elements[i]
        return representation + 'Bottom'
    
    
if __name__ == "__main__":
    stck = Stack()
    stck.push(1)
    stck.push(2)
    stck.push(3)
    print(stck)
    print('stack size:', stck.size())
    stck.pop()
    print(stck)
    print('stack size:', stck.size())
