# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. 
# The order does not matter.
# Follow-up: Can you do this in linear time and constant space?

TEST = [2, 4, 6, 8, 10, 2, 6, 10]

# O(n) time O(1) space PASS
def findTwo(lst : list):
    for i, x in enumerate(lst):
        if lst.count(x) > 1:
            lst.pop(i)
            lst.remove(x)
    return lst
print(findTwo(TEST))