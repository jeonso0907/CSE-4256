from math import gcd

# CSE 4256 Homework 9
# Sooyoung Jeon

class Fraction:

    #the constructor for the Fraction class
    #n is the numerator
    #d is the denominator
    #The constructor should create a Fraction object that is reduced
    def __init__(self, num, den = None):
        if den == None:
            div = num.index("/")
            den = int(num[div + 1:])
            num = int(num[:div])
        if den < 0:
            num *= -1
            den *= -1
        div = gcd(num, den)
        self.num = num // div
        self.den = den // div

    #Returns a string representation of self. This is needed to print Fractions in a list correctly.
    def __repr__(self):
        return str(self.num / self.den)

    #If f and g are Fractions, then f * g returns a Fraction that is the
    # sum of f and g
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    #If f is a Fractions, then ~f returns a Fraction that is the
    #reciprocal of f
    def __invert__(self):
        return Fraction(self.den, self.num)

    #If f is a Fractions, then -f returns a Fraction that is the
    # negation of f.
    def __neg__(self):
        return Fraction(self.num * -1, self.den)

    #If f and g are Fractions, then f + g returns a Fraction that is the
    # sum of f and g
    def __add__(self, other):
        num_sum = self.num * other.den + other.num * self.den
        den_sum = self.den * other.den
        return Fraction(num_sum, den_sum)

    #If f and g are Fractions, then f - g returns a Fraction that is the
    # difference of f and g
    #You should implement this method without calling the constructor directly.
    def __sub__(self, other):
        num_sub = self.num * other.den - other.num * self.den
        den_sub = self.den * other.den
        return str(num_sub / den_sub)

    #If f and g are Fractions, then f / g returns a Fraction that is the
    # quotient of f and g
    #You should implement this method without calling the constructor directly.
    def __truediv__(self, other):
        num_quo = self.num * other.den
        den_quo = other.num * self.den
        return num_quo // den_quo

    #Returns true if self < other. False otherwise
    def __lt__(self, other):
        self_num = self.num * other.den
        other_num = other.num * self.den
        if self_num < other_num:
            return True
        return False

    #Returns the absolute value of self. If f is a Fraction, this is called as abs(f).
    def __abs__(self):
        if self.num < 0:
            self.num = self.num * -1
        return Fraction(self.num, self.den)

    ##Returns a string representation of self as a mixed number. For example, 12/5 as a mixed number is "2 2/5".
    def mixed_number(self):
        div = self.num // self.den
        new_num = self.num % self.den
        return str(div) + " " + str(new_num) + "/" + str(self.den)

#After you finish and test all of the methods above, you should modify the __init__ methods so that it can be passed a string
#representation of a fraction, such as "14/102". To do this, modify the definition of __init__ as shown below,

#__init__(self, n, d = None):

#In your code, check to see if d is None. If it is, then n holds the string representation. If d is not None,
#then n and d are integers representing the numerator and denominator respectively.

#Finally, modify your code so that the string can represent a number with
#a decimal. For example, "12.354".

f = Fraction("12/5")
g = Fraction(3, 4)
print(f / g)
