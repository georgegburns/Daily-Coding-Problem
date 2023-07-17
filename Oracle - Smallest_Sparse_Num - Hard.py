# We say a number is sparse if there are no adjacent ones in its binary representation. 
# For example, 21 (10101) is sparse, but 22 (10110) is not. 
# For a given input N, find the smallest sparse number greater than or equal to N.

# Do this in faster than O(N log N) time.
import math
    
# O (Log N) time
def binaryConverter(num : int):
    og = num
    bin = ''
    while num != 0:
        if num % 2 != 0:
            bin += '1'
        else:
            bin += '0'
        num = math.floor(num / 2)
    if '11' not in bin.split('0'):
        return og
    else:
        og = og-1
        return binaryConverter(og)

print(binaryConverter(21))
print(binaryConverter(22))
print(binaryConverter(6))

