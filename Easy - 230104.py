# This problem was asked by Microsoft.
# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

import math

def Median(lst : list):
    for i in range(len(lst)):
        # division by zero catch
        if i == 0:
            print(lst[0])
        else:
            # creating a list up to the current index
            temp = lst[:i+1]
            # sorting the list
            temp.sort()
            # if the length of the list is even then there are two middle numbers
            if len(temp) % 2 == 0:
                # establishing those numbers and then dividing by 2
                lower = int((len(temp)/2) - 1)
                upper = int(len(temp)/2)
                middle = temp[lower] + temp[upper]
                median = middle/2
                # if that median number is even then converting to int
                if median % 2 == 0:
                    print(int(median))
                else:
                    print(median)
            else: 
                # if the length of the list is odd, finding the middle index (median)
                median = math.floor(len(temp)/2)
                print(temp[median])

# returns: 2, 1.5, 2, 3.5, 2, 2, 2                  
test = [2,1,5,7,2,0,5]

Median(test)