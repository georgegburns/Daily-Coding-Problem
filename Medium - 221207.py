# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

import types

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

#defining two functions that take a and b and return the relevant input
def car(a,b):
    return a

def cdr(a,b):
    return b

#calling the pair function into a variable
x = cons(3,4)

#placing the car and con function into the f variable of pair
print(x(car))
print(x(cdr))