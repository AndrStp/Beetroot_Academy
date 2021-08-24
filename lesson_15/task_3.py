# Write a class TypeDecorators which has several methods for converting results of functions to a specified type 
# (if it's possible):

# methods:
# to_int
# to_str
# to_bool
# to_float

# Don't forget to use @wraps
# ```
# class TypeDecorators:
#     pass

# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string

# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string

# assert do_nothing('25') == 25
# assert do_something('True') is True
# ```


class TypeDecorators:
    """Converts results of given functions to a specified type
    if possible. Otherwise raises ValueError"""

    def to_int(self):
        """Convert the result of a function to int"""
        def wrapper(*args, **kwargs):
            try:
                return int(self(*args, **kwargs))
            except ValueError as v_e:
                return f'{v_e} occured'
            except TypeError as t_e:
                return f'{t_e} occured'
        return wrapper

    def to_str(self):
        """Convert the result of a function to int"""
        def wrapper(*args, **kwargs):
            try:
                return str(self(*args, **kwargs))
            except ValueError as v_e:
                return f'{v_e} occured'
            except TypeError as t_e:
                return f'{t_e} occured'
        return wrapper

    def to_bool(self):
        """Convert the result of a function to int"""
        def wrapper(*args, **kwargs):
            try:
                return bool(self(*args, **kwargs))
            except ValueError as v_e:
                return f'{v_e} occured'
            except TypeError as t_e:
                return f'{t_e} occured'
        return wrapper

    def to_float(self):
        """Convert the result of a function to int"""
        def wrapper(*args, **kwargs):
            try:
                return float(self(*args, **kwargs))
            except ValueError as v_e:
                return f'{v_e} occured'
            except TypeError as t_e:
                return f'{t_e} occured'
        return wrapper
            

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string


if __name__ == '__main__':
    print(do_nothing('10'))  # -> 10
    print(do_something([]))  # False

    assert do_nothing('25') == 25
    assert do_something('True') is True