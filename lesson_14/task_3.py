# Write a decorator `arg_rules` that validates arguments passed to the function.

# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed; 
# otherwise, return the result.

# ```
# def arg_rules(type_: type, max_length: int, contains: list):
#     pass

# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
 
# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
# ```


def arg_rules(max_length: int, type_: str, contains: list):
    """Validates arguments passed to the function"""
    
    def arg_rules_decorator(func):
        def function_wrapper(arg):          
            if not isinstance(arg, str):
                print('Is not a string')
                return False

            if len(arg) > max_length:
                print('Exceeded max_length constraint')
                return False

            for el in contains:
                if el not in arg:
                    print('Does not contain required elements')
                    return False
            
            return func(arg)
        
        return function_wrapper
    
    return arg_rules_decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
 
assert create_slogan('johndoe05@gmail.com') is False # -> Exceeded max_length constraint
assert create_slogan(123761278367812736871286) is False # -> Is not a string
assert create_slogan('john@gmail.com') is False # -> Does not contain required elements
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
