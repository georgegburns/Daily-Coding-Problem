# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

#defining two functions that take cons(a,b) and return the relevant input using the .__closure__ attribute
def car(f):
    #referencing the relevant index
    return f.__closure__[0].cell_contents

def cdr(f):
    return f.__closure__[1].cell_contents

#outputs
print(car(cons(3,4)))
print(cdr(cons(3,4)))
