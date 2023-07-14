# Given an integer n, 
# return the length of the longest consecutive run of 1s in its binary representation.

# For example, given 156, you should return 3.

import math

TEST = 156

def binaryGen(num : int):
    i = num
    binary = ""
    while i !=0:
        i = math.floor(num / 2)
        binary += str(num % 2)
        num = i
        print(i)
        print(binary)
    return binary
        
def oneCounter(binary : str):
    binary = binary.split('0')
    result = sorted(binary, key=lambda x : len(x))[-1]
    return result
        
# returns 111 PASS
print(oneCounter(binaryGen(TEST)))

