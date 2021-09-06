"""
Basics, import, work with os module

Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, 
for additional info about it follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS 
or Linux - just call manual for this utility via command: `man wc`).

Create a Python module called `mymod.py`, which has three functions:

* count_lines(name) function that reads an input file and counts the number of lines in it 
(hint: file.readlines() does most of the work for you, and `len` does the rest) 

* count_chars(name) function that reads an input file and counts the number of characters in it 
(hint: file.read() returns a single string)

* test(name) function that calls both counting functions with a given input file­name. 

Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a command-line 
via the sys.argv list; for now, assume it’s a passed-in function argument.
All three `mymod.py` functions should expect a filename string to be passed in. 

Test your module interactively, using import and name qualification to fetch your exports. 

Does your PYTHONPATH need to include the directory where you created mymod.py?

Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice; 
if you’re feeling ambitious, you may be able to improve this by passing an open file object into the two count functions 
(hint: file.seek(0) is a file rewind).
"""

from sys import argv
from os import path


def main():
    """Mimics the 'wc' command except for word count"""

    try:
        result = test(take_agrs())
        print(result)

    except ValueError as v_err:
        print(v_err)

    except FileNotFoundError as f_err:
        print(f_err) 
    

def take_agrs():
    """Returns the args given by the user"""
    
    args = argv

    if len(args) > 2:
        raise ValueError (f'Too many args. Expected 2, got {len(args)} instead.')
    
    if not path.isfile(args[1]):
        raise FileNotFoundError (f'The file with name "{args[1]}" does not exist.')
    
    return args[1]


def test(name: str) -> tuple:
    """Reads an input file and returns the tuple of 
    number of lines and number of characters """

    return count_lines(name), count_chars(name)


def count_lines(name: str) -> int:
    """Reads an input file and counts the number of lines in it"""

    with open(name, 'r') as f:
        return len(f.readlines())


def count_chars(name: str) -> int:
    """Reads an input file and counts the number of characters in it"""
    
    with open(name, 'r') as f:
        return len(f.read())


if __name__ == '__main__':
    main()