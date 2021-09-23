"""
Task 3

Extend the Queue to include a method called get_from_stack that searches and 
returns an element e from a queue. Any other element must remain in the queue 
respecting their order. Consider the case in which the element is not found - 
raise ValueError with proper info Message
"""


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
    
    def get_from_queue(self, e):
        temp_q = Queue()

        result = None
        for _ in range(self.size()):
            item = self.dequeue()
            if item == e:
                result = item
                continue
            temp_q.enqueue(item)

        for _ in range(temp_q.size()):
            self.enqueue(temp_q.dequeue())
        
        if not result:
            raise ValueError('Item is not found!')

        return result


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print('Queue before get:\n', q)

    try:
        print('Get item: ', q.get_from_queue(5))
    except ValueError as e:
        print(e)

    print('Queue after get:\n', q)
