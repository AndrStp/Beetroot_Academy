# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then 
# returns the value of squared a divided by b, construct a try-except block which raises an exception 
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).


def square() -> float:
    """Returns the value of squared a divided by b"""
    while True:
        try:
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            return f'The result is {a**2 / b}'

        except ValueError:
            print('The inputs should be digits only!')

        except ZeroDivisionError:
            print('The second number should be greater than 0!')
        
        except KeyboardInterrupt:
            print('\nBye!')
            quit()


result = square()
print(result)
