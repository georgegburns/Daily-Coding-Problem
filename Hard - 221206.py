# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def lowest_pos(lst):
    lst_set = set(lst)
    pos_lst = []
    value = 0
    for i in lst_set:
        if i > 0:
            value = 1
            pos_lst.append(i)
    if value == 0:
        lowest = 1
    else:
        for i in range(len(pos_lst)):      
            if i == len(pos_lst)-1:
                lowest = pos_lst[i] + 1
                break
            elif pos_lst[i] > 0:
                x = pos_lst[i+1]
                if x - pos_lst[i] != 1:
                        lowest = pos_lst[i] + 1
                        break            
    return lowest
    
#test 1
lst = [3,4,-1,1]
 
print(lowest_pos(lst))

#test 2
lst = [1,2,0]
 
print(lowest_pos(lst))

#test 3
lst = [-2,-3,-5]

print(lowest_pos(lst))

#test 4
lst = [1,2,2,3]

print(lowest_pos(lst))