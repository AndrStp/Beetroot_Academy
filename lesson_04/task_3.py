def main():
    name = 'andrey'
    greeting = 'Hi stranger! You are asked to guess my name. Have fun! :)'
    instruction = 'type "exit" to stop'
    print(greeting, instruction, sep='\n')

    flag = True
    while flag:
        guess = input('Enter your guess: ')
        if guess.lower() == 'exit':
            quit()
        if check_name(name, guess):
            print(f'You\'ve guessed my name!')
            flag = False
        else:
            print(f'Sorry, it\'s not my name!')


def check_name(name_: str, guess_: str) -> bool:
    """Returns whether your name equals mine"""
    if guess_.lower() == name_:
        return True
    else:
        return False


main()