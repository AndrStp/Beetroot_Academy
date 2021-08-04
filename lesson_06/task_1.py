# Make a program that has some sentence (a string) on input and returns a dict 
# containing all unique words as keys and the number of occurrences as values. 

# For testing:
# 'Hello, my name is Andrey. Andrey is from Odessa. Andrey currently studies python language at Beetroot Academy in Python for Begginers course. Beetroot Academy is a great place to learn python!'

import string


raw_text = input('Enter your text here: ')

# get rid of punctuation in a raw_string
processed_text = raw_text.translate(str.maketrans('', '', string.punctuation))

# count words in a dict
words = {}
for word in processed_text.split():
    word = word.lower()
    words[word] = words.get(word, 0) + 1

print(words)