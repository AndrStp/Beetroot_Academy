"""
Task 3

Extend the Stack to include a method called get_from_stack that searches and returns 
an element e from a stack. Any other element must remain on the stack respecting 
their order. Consider the case in which the element is not found - 
raise ValueError with proper info Message
"""

from copy import copy


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
    
    def get_from_stack(self, e):
        index = self.search_element(e)
        if index == -1:
            raise ValueError('Item is not found!')

        temp_stack = Stack()
        for i in range(index):
            temp_stack.push(self.pop())
        item = self.pop()

        for i in range(index):
            self.push(temp_stack.pop())

        return item

    def search_element(self, e) -> int:
        temp = copy(self._items)
        for i in range(len(self._items)):
            if temp.pop() == e:
                return i
        return -1                  


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print('Stack before get:\n', s)

    try:
        print('Get item: ', s.get_from_stack(5))
    except ValueError as e:
        print(e)

    print('Stack after get:\n',  s)
