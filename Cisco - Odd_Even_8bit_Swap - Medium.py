# This problem was asked by Cisco.
# Given an unsigned 8-bit integer, swap its even and odd bits. 
# The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
# Bonus: Can you do this in one line?

n = 10101010
# n = 11100010

onelineSWAP = ''.join([str(n)[i]+str(n)[i-1] for i in range(len(str(n))) if i%2!=0])

print(onelineSWAP)
