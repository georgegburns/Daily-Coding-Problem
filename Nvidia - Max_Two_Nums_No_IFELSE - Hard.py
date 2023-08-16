# Find the maximum of two numbers without using any
# if-else statements, branching, or direct comparisons.

num1 = 10
num2 = 2

def maximumNum(num1, num2):
    return ord(sorted([chr(num1), chr(num2)], reverse=True)[0])

print(maximumNum(num1,num2))