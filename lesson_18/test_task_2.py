# Write tests for the Phonebook application, which you have implemented in module 1. 
# Design tests for this solution and write tests using unittest library.


# test_phonebook_methods.py

import os
import phonebook_methods as methods


test_phonebook = {
    "contacts": [
        {
            "number": "+1300400500",
            "first_name": "John",
            "last_name": "Johnson",
            "city": "New York"
        },
        {
            "number": "+380487005040",
            "first_name": "Luda",
            "last_name": "Golova",
            "city": "Odessa"
        }
    ]
}



def test_load_book():
    """Check that load book returns dict (json)"""
    assert isinstance(methods.load_book(), dict)


def test_save_book():
    """Checks whether the method writes json to the file"""
    file_size_before = os.path.getsize('data_phonebook.json')
    methods.save_book(test_phonebook)
    file_size_after = os.path.getsize('data_phonebook.json')
    assert file_size_before != file_size_after


def test_not_none_read_book():
    """Checks whether the phonebook is returned"""
    assert methods.read_book(test_phonebook) is not None


def test_type_read_book():
    """Checks whether the returned phonebook is of string type"""
    assert isinstance(methods.read_book(test_phonebook), str)



# clear phonebook
methods.save_book({})