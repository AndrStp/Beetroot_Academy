# Extracting numbers.

# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

numbers = list(range(1, 101))

integers = [x for x in numbers if x % 7 == 0 and x % 5]

print(integers)