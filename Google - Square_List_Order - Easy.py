# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

def productOrdered(lst : list):
    PRODUCT_ORDERED = sorted([x**2 for x in lst])
    return PRODUCT_ORDERED

# Returns [0, 4, 4, 9, 81] PASS
TEST = [-9, -2, 0, 2, 3]

print(productOrdered(TEST))