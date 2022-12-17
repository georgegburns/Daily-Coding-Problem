#Given an array of integers that are out of order, determine the bounds of the smallest
#window that must be sorted for the entire array to be sorted.
#For example given [3,7,5,6,9], you should return (1,3)

#iteration 1 (fails on test 2)
def smallest_window(array : list):
    x , y = None,None
    ordered_list = sorted(array)
    for i in range(len(ordered_list)):
        if array[i] != ordered_list[i]:
            x = i
            break
    for i in range(len(ordered_list)):
        if array[i] != ordered_list[i]:
            y = i
    return x , y
        
#test1
test = [3,7,5,6,9]

print(smallest_window(test))

#test2
test = [100, 1, 2, 3, 4]

print(smallest_window(test))
