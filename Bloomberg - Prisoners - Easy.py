# There are N prisoners standing in a circle, waiting to be executed. 
# The executions are carried out starting with the kth person, 
# and removing every successive kth person going clockwise until there is no one left.

# Given N and k, write an algorithm to determine 
# where a prisoner should stand in order to be the last survivor.

# For example, if N = 5 and k = 2, 
# the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

# Bonus: Find an O(log N) solution if k = 2.

import math
N = 5
k = 2

def lastSurvivor(N : int, k : int):
    survivors = list(range(1, N+1))
    for i in survivors:
        survivors.pop(k-1)
        survivors = survivors[::-1]
        if len(survivors) % k != 0:
            return survivors[len(survivors) % k]

print(lastSurvivor(N, k))