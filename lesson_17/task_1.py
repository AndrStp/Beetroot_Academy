# Create your own implementation of a built-in function enumerate, named `with_index`, # which takes two parameters: 
# `iterable` and `start`, default is 0. # Tips: see the documentation for the enumerate function



def with_index(iterable, start: int = 0):
    """Substitute for enumerate function. 
    Returns the generator object that yields tuple pairs of number 
    from 0 (default) and an element from the given iterable object"""
    for i in range(len(iterable)):
        yield i+start, iterable[i]


some_iterbale = 'python'

for el in with_index(some_iterbale, start=1):
    print(el, end=(', ' if el[1] != some_iterbale[-1] else '\n'))
