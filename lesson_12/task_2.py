# Mathematician


# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:

# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

# class Mathematician:
#     pass

# m = Mathematician()

# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

from calendar import isleap


class Mathematician:
    def square_nums(self, nums: list) -> list:
        return [x**2 for x in nums]

    def remove_positives(self, nums: list) -> list:
        return [x for x in nums if x < 0]

    def filter_leaps(self, dates: list) -> list:
        ### using calendar module
        return [year for year in dates if isleap(year)]

        ### using custom function
        # def leap(year: int) -> bool:
        #     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
        # return [year for year in dates if leap(year)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
