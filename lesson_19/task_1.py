"""
Imports practice

Make a directory with 2 modules; make a function in one of them; 
then import this function in the other module and use that in your script of choice.
"""

from some_module import some_func_from_module


def func():
    return 0


result = func() # use func from the current script
other_result = some_func(result)  # passing the result to the imported func
print(other_result)