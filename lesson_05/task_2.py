# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint


list_1 = [randint(1, 10) for _ in range(10)]
list_2 = [randint(1, 10) for _ in range(10)]

list_3 = list(set(list_1) & set(list_2))

if list_3:
    print('Common items between two lists are: ', end = '')
    print(*list_3, sep=', ')
else:
    print('There are no common elemetns between two lists')