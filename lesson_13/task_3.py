# Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
# If all nums inside the list are positive, execute the first function on that list and return the result of it. 
# Otherwise, return the result of the second one


def choose_func(nums: list, func1, func2) -> int:
    nums_positive = all([num for num in nums if num > 0])
    nums_negative = all([num for num in nums if num < 0])
    if nums_positive:
        return func1(nums)
    else:
        return func2(nums)


print(choose_func([1, 2, 3, 4], max, min)) # -> 4
print(choose_func([-1, -2, -3, -4], max, min)) # -> -1