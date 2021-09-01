# Custom exception

# Create your custom exception named `CustomException`, you can inherit from base Exception class, 
# but extend its functionality to log every error message to a file named `logs.txt`. 
# Tips: Use __init__ method to extend functionality for saving messages to file


# class CustomException(Exception):
# def __init__(self, msg):

from os import path
from datetime import datetime


class CustomException(Exception):
    """Custom exception class"""

    def __init__(self, msg) -> None:
        self.msg = msg 
        self.file_name = 'task_4_logs.txt'
        self.date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        if path.exists(self.file_name):
            mode = 'a'
        else:
            mode = 'w'

        with open(self.file_name, mode, encoding='utf-8') as f:
            f.write(f'{self.msg} raised on {self.date_time}\n')


exception_1 = CustomException('Error')

raise exception_1