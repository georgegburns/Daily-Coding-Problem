#Given an array of numbers, find the maximum sum of any continuous subarray of the array.
#For example, given [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would
#take elements 42, 14, -5 and 86. Given the array [-5, -1, -8, -9] the sum would be 0, since we
#would choose not to take any elements. 

#Do this in O(n) time.

def max_subarray(array : list):
    maximum = 0
    for i in range(len(array) - 1):
        for x in range(i, len(array)):
            maximum = max(maximum, sum(array[i:x+1]))
    return maximum

test = [34,-50,42,14,-5,86]

print(max_subarray(test))
            
test = [-5, -1, -8, -9] 

print(max_subarray(test))

def max_subarray_v2(array : list):
    max_end = max_curr = 0
    for x in array:
        max_end = max(x, max_end + x)
        max_curr = max(max_curr, max_end)
    return max_curr
    
test = [34,-50,42,14,-5,86]

print(max_subarray_v2(test))
            
test = [-5, -1, -8, -9] 

print(max_subarray_v2(test))