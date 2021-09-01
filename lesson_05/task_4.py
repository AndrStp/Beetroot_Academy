# The math quiz program

# Write a program that asks the answer for a mathematical expression, checks whether 
# the user is right or wrong, and then responds with a message accordingly.

from random import randint, choice

def main():
    """Runs the math quiz"""
    expression = generate_expression()
    answer = solve_expression(expression)
    print('The math quiz is the following:\n')
    print(expression, '\n')
    user_answer = input('Enter your answer here: ')
    if user_answer == str(answer):
        print('Right! Well done!\n')
    else:
        print(f'Wrong! The correct answer is {answer}\n')


def generate_expression() -> str:
    """Generates the expression for assessment"""
    operands = ['+', '-', '*', '/', '**']
    operand = choice(operands)
    a = randint(1, 100)
    b = randint(1, 10)
    return f'{a} {operand} {b}'

def solve_expression(expression: str) -> int or float:
    """Returns the result of evaluation of expression"""
    return eval(expression)


if __name__ == '__main__':
    main()
