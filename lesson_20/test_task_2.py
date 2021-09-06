"""
Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything 
works as designed. And also, write tests when your class raises errors or you have errors 
in the runtime context suite.
"""

# test_task_1.py

import pytest
import task_1


def test_file_not_found_1():
    """Should raise 'FileNotFoundError'"""
    with pytest.raises(FileNotFoundError):
        task_1.FileManager('new_file.txt', 'r')

def test_file_not_found_2():
    """Should create new file and write 'Hello' to it"""
    with task_1.FileManager('new_file.txt', 'w') as f:
        print('Hello', file=f, flush=True)
        assert len(f.read()) != 0

def test_file_mode_not_exist():
    """Should raise 'ValueError' for invalid file-mode"""
    with pytest.raises(ValueError):
        task_1.FileManager('text.txt', 'a+')

def test_file_mode_r():
    """Checks that 'text.txt.read()' return the string of non-zero len"""
    with task_1.FileManager('text.txt', 'r') as f:
        assert len(f.read()) != 0


