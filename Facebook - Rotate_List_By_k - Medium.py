# Write a function that rotates a list by k elements. 
# For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
# Try solving this without creating a copy of the list. 
# How many swap or move operations do you need?

def rotateBy(lst : list, k : int):
    """
    How many swap or move operations do you need?
    
    Answer: K squared

    """
    k_power = k * k
    rotations = 0
    while rotations < k_power:
        lst.insert(0,lst[-1])
        lst.pop(-1)
        rotations += 1
    return lst
        
# Produces [3, 4, 5, 6, 1, 2] PASS
test = [1, 2, 3, 4, 5, 6]

print(rotateBy(test, 2))
