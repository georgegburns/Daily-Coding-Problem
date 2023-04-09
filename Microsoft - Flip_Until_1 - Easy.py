# You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. 
# The ones that come up heads you flip again. 
# How many rounds do you expect to play before only one coin remains?
# Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
import math


def roundstillOne(n : int):
    count = 1
    while True:
        n = n/2
        if math.ceil(n) == 1 or n == 1:
            break
        count += 1
    return count

print(roundstillOne(2))