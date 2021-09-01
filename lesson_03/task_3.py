def calculator():
    """Returns result of simple calculations"""
    print('Greetings, it\'s a simple calculator\n\
actions to use:\n\
Addition -> add (+)\n\
Subtraction -> sub (-)\n\
Division -> div (/)\n\
Multiplication -> mult (*)\n\
Exponent (Power) -> pow (**)\n\
Modulus -> mod (%)\n\
Floor division -> floor (//)\n')
    a = int(input('Provide first number: '))
    b = int(input('Provide second number: '))
    operator = input('Enter your operator: ')

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def div(a, b):
        return a / b

    def mult(a, b):
        return a * b

    def mod(a, b):
        return a % b

    def floor(a, b):
        return a // b

    if operator == 'add':
        result = add(a, b)
    elif operator == 'sub':
        result = sub(a, b)
    elif operator == 'div':
        result = div(a, b)
    elif operator == 'mult':
        result = mult(a, b)
    elif operator == 'mod':
        result = mod(a, b)
    elif operator == 'floor':
        result = floor(a, b)

    print(f'The result of {a} {operator} {b} is: {result}')

    
calculator()