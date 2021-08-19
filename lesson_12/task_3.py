# Fraction

# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) 
# with appropriate checking and error handling

from __future__ import annotations
from math import gcd


class Fraction:
    """Represents a class for positive only integer-composed-fractions
    So fractions like '-(1/2)' or '0.2/1.5' will cause an error"""

    def __init__(self, numerator, denominator) -> None:
        if not isinstance(numerator, int):
            raise TypeError('The numerator should be an integer')
        elif numerator < 1:
            raise ValueError('The numerator should be a positive integer bigger than 0')

        if not isinstance(denominator, int):
            raise TypeError('The denominator should be an integer')
        elif denominator < 1:
            raise ValueError('The denominator should be a positive integer bigger than 0')

        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self) -> str:
        return f'({self.numerator} / {self.denominator})'

    def __str__(self) -> str:
        return f'({self.numerator} / {self.denominator})'
    
    @staticmethod
    def is_fraction(object) -> bool:
        """Returns True if object is an object of Fraction class
        False - otherwise"""
        if isinstance(object, Fraction):
            return True
        else:
            return False
    
    @staticmethod
    def get_least_common_denom(denom_1: int, denom_2: int) -> int:
        """Returns common denominator for denom_1 and denom_2"""
        return int(denom_1 * denom_2 / gcd(denom_1, denom_2))

    @staticmethod
    def simplify_fraction(fraction: Fraction) -> Fraction:
        """Return the fraction by dividing both numerator and denominator by a gcd. 
        Returns the same fraction if the gcd equals 1"""
        common_gcd = gcd(fraction.numerator, fraction.denominator)
        if common_gcd == 1:
            return fraction
        else:
            return Fraction(int(fraction.numerator / common_gcd), int(fraction.denominator / common_gcd))


    def __gt__(self, other: Fraction) -> bool:
        """Returns True if the fraction is bigger than the other fraction
        False - otherwise"""
        if not Fraction.is_fraction(other):
            raise TypeError (f'Cannot compare {__class__.__name__} with {type(other)}')

        if self.denominator == other.denominator:
            return self.numerator > other.numerator

        self_numerator = self.numerator * (Fraction.get_least_common_denom(self.denominator, other.denominator) / self.denominator)
        other_numerator = other.numerator * (Fraction.get_least_common_denom(self.denominator, other.denominator) / other.denominator)
        return self_numerator > other_numerator

    def __add__(self, other: Fraction) -> Fraction:
        """Return the Fraction by adding other Fraction to it"""
        if not Fraction.is_fraction(other):
            raise TypeError (f'Cannot add {type(other)} with {__class__.__name__}')

        denominator = Fraction.get_least_common_denom(self.denominator, other.denominator)
        numerator = int(
            self.numerator * (denominator / self.denominator)
            + other.numerator * (denominator / other.denominator)   
        )
        return Fraction.simplify_fraction(Fraction(numerator, denominator))

    def __sub__(self, other: Fraction) -> Fraction:
        """Return the Fraction by adding other Fraction to it"""
        if not Fraction.is_fraction(other):
            raise TypeError (f'Cannot substract {type(other)} from {__class__.__name__}')

        if other > self:
            raise ValueError (f'The {other} cannot be greater than {self}')

        denominator = Fraction.get_least_common_denom(self.denominator, other.denominator)
        numerator = int(
            self.numerator * (denominator / self.denominator)
            - other.numerator * (denominator / other.denominator)   
        )
        return Fraction.simplify_fraction(Fraction(numerator, denominator))
    
    def __mul__(self, other: Fraction) -> Fraction:
        """Return the Fraction by multiplying it by other Fraction"""
        if not Fraction.is_fraction(other):
            raise TypeError (f'Cannot substract {type(other)} from {__class__.__name__}')

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction.simplify_fraction(Fraction(numerator, denominator))

    def __truediv__(self, other: Fraction) -> Fraction:
        """Return the Fraction by diving it by other Fraction"""
        if not Fraction.is_fraction(other):
            raise TypeError (f'Cannot substract {type(other)} from {__class__.__name__}')
        
        temp_other = Fraction(other.denominator, other.numerator)
        return self.__mul__(temp_other)