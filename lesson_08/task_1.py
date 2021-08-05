# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?


def oops() -> None:
    """Raises an exception"""
    raise IndexError
    # raise KeyError


def another_oops() -> None:
    """Calls oops()"""
    try:
        oops()
    except Exception:  # так делать нельзя :)
        print('Exception catched')


another_oops()