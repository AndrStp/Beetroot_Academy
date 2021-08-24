# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

# For example:
#  "add called with 4, 5"

# ```
# def logger(func):
#     pass

# @logger
# def add(x, y):
#     return x + y

# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
# ```


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} called with ', end='')
        print(*args, sep=', ')
        func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(3, 4)
square_all(3, 4, 5)