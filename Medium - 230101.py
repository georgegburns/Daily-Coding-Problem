# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. 
# Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, 
# and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def waterTrapped(lst : list):
    water = 0
    if lst[0] < lst[-1]:
        limit = lst[0]
    else: 
        limit = lst[-1]
    for i in range(1, len(lst) - 1):
        water += limit - lst[i]
    return water

# # produces 1
# test = [2,1,2]

# print(waterTrapped(test))

# # produces 8
# test = [3, 0, 1, 3, 0, 5]

# print(waterTrapped(test))

# # should produce 9 but produces 6 due to the middle being larger than the outer indexes
# test = [3, 0, 4, 1, 4, 0, 3]

# print(waterTrapped(test))

def waterTrapped(lst : list):
    water = 0
    if lst[0] < lst[-1]:
        x = lst[0]
        limit = x
        for i in range(1, len(lst)):
            if lst[i] < limit:
                water += limit - lst[i]
            elif lst[i] == limit:
                limit = x
            else: 
                limit = lst[i]
                water += limit - lst[i]
            # print(f'water: {water}')
            # print(lst[i])
            # print(f'limit: {limit}')
    else: 
        x = lst[-1]
        limit = x
        for i in range(0, len(lst) - 1):
            if lst[i] < limit:
                water += limit - lst[i]
            elif lst[i] == limit:
                limit = x
            else: 
                limit = lst[i]
                water += limit - lst[i]
            # print(f'water: {water}')
            # print(lst[i])
            # print(f'limit: {limit}')
    
    return water

# produces 1
test = [2,1,2]

print(waterTrapped(test))

# produces 8
test = [3, 0, 1, 3, 0, 5]

print(waterTrapped(test))

# dips in the middle : produces 9
test = [3, 0, 4, 1, 4, 0, 3]

print(waterTrapped(test))

# uneven start and endpoint : produces 14 
test = [3, 0, 3, 4, 0, 4, 5, 0, 5, 2, 0, 2]

print(waterTrapped(test))