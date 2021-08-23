# Write a Python program to detect the number of local variables declared in a function.

def func(*args) -> int:
    return len(args)


print('the number of locals is: ', func(1, 2, 3, 4))