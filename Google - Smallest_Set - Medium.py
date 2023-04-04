# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
# If there are multiple smallest sets, return any of them.
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.


TEST = [[0, 3], [2, 6], [3, 4], [6, 9]]

def smallestSETS(lst : list):
    # Getting a set of each integer in the 2d matrix
    SET = list(set([x for y in lst for x in y]))
    
    # Iterating through the SET twice to match each int with another int
    for i in range(len(SET)-1):
        for j in range(i, len(SET)-1):
            a, b = SET[i], SET[j]
            num = 0
            # Iterating through the top level of the original 2d matrix
            for TUP in lst:
                # If either a or b is in the pair then add to num
                if a in TUP or b in TUP:
                    num += 1
                else:
                    break
            # If all pairs have at least a or b then return {a,b}
            if num == len(lst):
                return {a,b}
         
# Returns {3,6} PASS           
print(smallestSETS(TEST))