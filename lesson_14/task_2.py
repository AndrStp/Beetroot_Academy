# Write a Python program to access a function inside a function 
# (Tips: use function, which returns another function)


def func(func_name: str):

    def func_1():
        print("I'm func_1")

    def func_2():
        print("I'm func_1")

    def func_3():
        print("I'm func_1")
    
    all_func = {
        'func_1': func_1,
        'func_2': func_2,
        'func_3': func_3
    }

    return all_func.get(func_name, 'no such func')


func_1 = func('func_1')
func_1() # -> I'm func_1

