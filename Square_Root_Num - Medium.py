# Given a real number n, find the square root of n. 
# For example, given n = 9, return 3.

def squareRoot(num : int):
    root = num ** 0.5
    return root

TEST = 9

# Returns 3 PASS
print(squareRoot(TEST))