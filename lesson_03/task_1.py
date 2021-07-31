string_ = input('Provide a string here: ')

def slice_string(strng: str) -> str:
    """Return first and last two chars in the word.
    If the word consists of less than 2 chars return empty string"""
    if len(strng) < 2:
        return ''
    else:
        return strng[:2] + strng[-2:]


print(slice_string(string_))