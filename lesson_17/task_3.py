# Create your own implementation of an iterable, which could be used inside for-in loop. 
# Also, add logic for retrieving elements using square brackets syntax.


class MyIterable:
    def __init__(self, some_sequence) -> None:
        self.iterable = some_sequence
        
    def __getitem__(self, index):
        print(f'{self.__getitem__.__name__} is called with index: {index}')
        return self.iterable[index]


l = MyIterable([1, 2, 3, 4])

print(l[0]) # -> 1
print(l[:2]) # -> [1, 2]

for i in l:
    print(i)

#==================================================================================

def squares():
    i = 1
    while True:
        yield i**2
        i += 1

sq_generator = squares()

for i in range(0, 50):
    if i % 5 == 0:
        print()
    print(str(next(sq_generator)).rjust(5), end=' ')



