"""
Pytest fixtures with context manager

Create a simple function, which performs any logic of your choice with text data, 
which it obtains from a file object, passed to this function ( def test(file_obj) ).

Create a test case for this function using pytest library (https://docs.pytest.org/en/latest/contents.html).

Create pytest fixture, which uses your implementation of the context manager to return a file object, 
which could be used inside your function.
"""

import pytest
import sys
from task_1 import FileManager


# @pytest.fixture
# def return_file_object(file_name: str):
#     with FileManager(file_name, 'r') as f:
#         return 


def test(file_obj) -> int:
    """Returns the size of an file object"""
    with file_obj as f:
        return sys.getsizeof(file_obj)