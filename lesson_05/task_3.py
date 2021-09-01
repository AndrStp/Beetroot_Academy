# Words combination

from random import shuffle


word = list(input('Enter a word: '))

for _ in range(5):
    shuffle(word)
    print(''.join(word))