#Given an array of integers, return a new array where each element in the new 
#array is the number of smaller elements to the right of that element in the 
#original array.

#For example, given the array [3,4,9,6,1] return [1,1,2,1,0]. 

def number_smallest(array : list):
    new_array = []
    for i in range(len(array)):
        count = 0
        for x in range(i, len(array)):
            if array[x] < array[i]:
                count += 1
        new_array.append(count)     
    return new_array

#produces [1,1,2,1,0] - pass
test = [3,4,9,6,1]

print(number_smallest(test))

#produces [0,0,0,0,0] - pass
test = [1,1,1,1,1]

print(number_smallest(test))