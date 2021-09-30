"""
Task 1

Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, 
which will take two parameters `start` and `stop`, and return a copy of the list starting at 
the position and going up to but not including the stop position.
"""

from node import Node


class UnorderedList:

    def __init__(self) -> None:
        self._head = None
        self._size = 0
    
    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._head is None

    def add(self, item) -> None:
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
        self._size += 1
    
    def append(self, item) -> None:
        current = self._head
        if current:
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self._head = Node(item)
        self._size += 1
    
    def insert(self, index, item):
        """Inserts the item to the given index. 
        Index should start from zero"""
        if index >= self._size:
            raise ValueError('Index >= List size')
        elif index < 0:
            raise ValueError('Negative index')
        
        if index == 0:
            self.add(item)
        
        else:
            previous = None
            current = self._head
            while index:
                previous = current
                current = current.get_next()
                index -= 1

            new_node = Node(item)
            previous.set_next(new_node)
            new_node.set_next(current)
        self._size += 1

    def search(self, item) -> bool:
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def get_index(self, item) -> int:
        """Return index of the item. Index starts with 0"""
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        return -1

    def remove(self, item) -> None:
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self._size -= 1
    
    def pop(self):
        current = self._head
        if not current:
            raise Exception("List is empty")

        if current.get_next() == None:
            self._head = None
        else:
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
        self._size -= 1
    
    def get_slice(self, start, stop):
        """Return the slice of the current List.
        The slice is the UnorderedList instance.
        Start and stop should be non-negative integers"""
        if start < 0 or stop > self._size or start > stop:
            raise ValueError('Invalid values for either start of stop')
        elif (stop - start) == 0:
            return None
        
        slice_ = UnorderedList()

        index = 0
        current = self._head
        while index < stop:
            if index >= start:
                slice_.append(current.get_data())
            current = current.get_next()
            index += 1
        return slice_

    def __repr__(self) -> str:
        representation = "<UnorderedList: Head->"
        current = self._head
        while current is not None:
            representation += f"({current.get_data()})->"
            current = current.get_next()
        representation += "'null'"
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    print(my_list)
    my_list.pop()
    print(my_list)
    my_list.insert(1, 0)
    print(my_list)  
    print('Index of the \'0\' element is', my_list.get_index(0))
    print('Slice from 1 to 3:', my_list.get_slice(1, 2))
