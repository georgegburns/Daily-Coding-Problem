# Given a sorted array, 
# find the smallest positive integer that is not the sum of a subset of the array.

# For example, for the input [1, 2, 3, 10], you should return 7.

# Do this in O(N) time.


TEST = [1, 2, 3, 10]

def smallestInt(nums : list):
    result = 0 # 2, 4
    for num in nums:
        result += num
        if num + 1 not in nums and result < nums[-1]:
            break
    return result + 1

# Produces 7 in O(n) time PASS
print(smallestInt(TEST))