"""
File Context Manager class

Create your own class, which can behave like a built-in function `open`. 
Also, you need to extend its functionality with counter and logging. 
Pay special attention to the implementation of `__exit__` method, which has to 
cover all the requirements to context managers mentioned here:

https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager 
https://docs.python.org/3.7/reference/compound_stmts.html#with
"""

import logging
from os import path


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d %b %Y %H:%M:%S')


class FileManager:
    counter = 0

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, file_path, mode):
        logging.debug('Getting the parametres')

        if not path.isfile(file_path):
            raise FileNotFoundError (f'The file "{file_path}" does not exist')
        
        self.file_path = file_path

        if mode not in ['r', 'w', 'x', 'a']:
            raise ValueError (f'Unsupportable file-mode: "{mode}"')

        self.mode = mode
        
    def __enter__(self):
        FileManager.counter += 1
        self.file_handle = open(self.file_path, self.mode)
        logging.debug('Entering the context manager')
        return self.file_handle
    
    def __exit__(self, *exc):
        self.file_handle.close()
        logging.debug('Leaving the context manager')


if __name__ == '__main__':
    for _ in range(3):
        with FileManager('text.txt', 'r') as f:
            print(f.read())
        print()

    print(FileManager.get_counter())  # -> 3