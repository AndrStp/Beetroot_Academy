# The Guessing Game.

from random import randint


def game():
    number = randint(1, 10)
    print('The game is to guess the number range from [1 to 10]')

    i = 1
    flag = True
    while flag:
        guess = input('Enter your number: ')
        try:
            guess = int(guess)
        except ValueError:
            print('You should enter numbers only!')
            continue
        
        if guess > number:
            print('Your guess is bigger than the number')
        elif guess < number:
            print('Your guess is smaller than the number')
        else:
            print(f'You guessed the number: {number}. It took you {i} guesses')
            return

        i += 1


game()
