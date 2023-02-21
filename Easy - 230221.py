# This problem was asked by Snapchat.
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
# The input list is not necessarily ordered in any way.
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

test = [(1, 3), (2,3), (5, 8), (6,7), (4, 10), (20, 25)]

def intervalOverlap(arr : list):   
    arr = sorted(arr, key=lambda x : x[0])
    new_arr = []
    index = 0
    for i in range(1, len(arr)):
        if arr[index][1] >= arr[i][0]:
            x,y = (min(arr[index][0], arr[i][0]), max(arr[index][1], arr[i][1]))
            new_arr.append((x,y))
        else:
            new_arr.append(arr[index])
            index = index + 1
            arr[index] = arr[i]
            new_arr.append(arr[index])
    new_arr = sorted(set(new_arr), key=lambda x : x[0])
    print(new_arr)
    return new_arr
        
intervalOverlap(test)
