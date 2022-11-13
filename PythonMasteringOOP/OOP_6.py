import math
import antigravity


class Fraction:
    """A Fraction class that prints objects created its floating point values"""
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError(f'Numerator {numerator} must be an integer')
        if not isinstance(denominator, int):
            raise TypeError(f'Numerator {numerator} must be an integer')
        self.numerator = numerator
        self.denominator = denominator
        greatest_common_divisor = math.gcd(self.numerator, self.denominator)
        if greatest_common_divisor > 1:
            self.numerator = self.numerator
            self.denominator = self.denominator
        self.value = self.numerator/self.denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def __str__(self):
        output = f'Fraction {str(self.numerator)} / {str(self.denominator)}' \
                 f'\n Value: {self.value} \n'
        return output

    def get_value(self):
        return self.value

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError('Second value in attenpt to add is not a Fraction')
        new_denominator = math.lcm(self.denominator, other.denominator)
        mult_factor = new_denominator // self.denominator
        eq_numerator = self.numerator * mult_factor

        other_mult_factor = new_denominator // other.denominator
        other_frac_eq_numerator = other.numerator * other_mult_factor
        new_numerator = eq_numerator + other_frac_eq_numerator

        added_fraction = Fraction(new_numerator, new_denominator)
        return added_fraction

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        if (self.numerator == other.numerator) and \
           (self.denominator == other.denominator):
            return True
        else:
            return False


if __name__ == '__main__':
    o_fraction1 = Fraction(1, 3)
    o_fraction2 = Fraction(2, 5)
    print(f'Decimal value of fraction 1\n {o_fraction1}')
    print(f'Decimal value of fraction 2\n {o_fraction2}')
    sum_fraction = o_fraction1 + o_fraction2
    print(f'Sum is \n {sum_fraction}')
