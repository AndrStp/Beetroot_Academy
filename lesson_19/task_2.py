"""
The sys module.

The “sys.path” list is initialized from the PYTHONPATH environment variable. 
Is it possible to change it from within Python? If so, does it affect where Python looks for module files? 
Run some interactive tests to find it out.
"""


import sys


sys.path.append('/Users/andrey/Documents/Coding/beetroot/lesson_06')


from task_3_copy import integers


print(integers) # -> [7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98]