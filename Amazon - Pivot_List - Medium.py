# Given a pivot x, and a list lst, partition the list into three parts.
# •	The first part contains all elements in lst that are less than x
# •	The second part contains all elements in lst that are equal to x
# •	The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], 
# one partition may be [9, 3, 5, 10, 10, 12, 14].

TEST = [9, 12, 3, 5, 14, 10, 10]

# O(n) time O(n) space, [9,3,5,10,10,12,14] PASS
def partitionList(n : int, lst : list):
    FIRST = [x for x in lst if x < n]
    MIDDLE = [x for x in lst if x == n]
    END = [x for x in lst if x > n]
    return FIRST + MIDDLE + END
    
print(partitionList(10, TEST))

# O(n) time O(1) space, [5,9,3,10,10,14,12] PASS
def partitionOptimised(n : int, lst : list):
    for i in lst:
        if i < n:
            lst.remove(i)
            lst.insert(0, i)
        elif i > n:
            lst.remove(i)
            lst.append(i)
    return lst

print(partitionOptimised(10, TEST)) 
            
