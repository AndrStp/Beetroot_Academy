# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 
# `start`, `end`, # and optional step. Tips: See the documentation for `range` function


class Range:
    """Mimics the range function. Works only with step 1 or -1"""
    def __init__(self, start, stop, step=1) -> None:
        if start == stop:
            raise TypeError('The start cannot be equal to stop')

        if (start > stop) and step > 0:
            raise TypeError('The start cannot be bigger than stop with positive step')
        
        if (start < stop) and step < 0:
            raise TypeError('The stop cannot be bigger than start with negative step')
        
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__start == self.__stop:
            raise StopIteration

        val = self.__start
        self.__start += self.__step
        return val


if __name__ == '__main__':
    for in_range in (Range(1, 10, 1), Range(10, 1, -1)):
        for i in in_range:
            print(i, end=' ')
        print()

    # don't do this
    # for i in Range(1, 10, 2):
    #    print(i)