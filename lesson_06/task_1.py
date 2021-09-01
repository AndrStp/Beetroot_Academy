# The greatest number

# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint


numbers = [randint(1, 1000) for _ in range(10)]

biggest = max(numbers)

# without using max()
biggest_ = None
for number in numbers:
    if biggest_ is None:
        biggest_ = number
    elif biggest_ < number:
        biggest_ = number
        

print('Using max() ->', biggest)
print('Without max() ->', biggest_)