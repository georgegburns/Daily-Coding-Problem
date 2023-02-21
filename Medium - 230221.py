# This problem was asked by Google.

# You are given an N by M 2D matrix of lowercase letters. 
# Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. 
# That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.
# For example, given the following table:
# cba
# daf
# ghi
# This is not ordered because of the a in the center. 
# We can remove the second column to make it ordered:
# ca
# df
# gi
# So your function should return 1, since we only needed to remove 1 column.
# As another example, given the following table:
# abcdef
# Your function should return 0, since the rows are already ordered (there's only one row).
# As another example, given the following table:
# zyx
# wvu
# tsr
# Your function should return 3, since we would need to remove all the columns to order it.

test = [['c','b','a'],
        ['d','a','f'],
        ['g','h','i']]

test2 = [['a','b','c','d','e','f']]

test3 = [['z','y','x'],
         ['w','v','u'],
         ['g','h','i']]

test4 = [['a','y','x'],
         ['b','v','u'],
         ['c','h','i']]

def numOrdered(arr : list):
    # A list of the lowercase alphabet to use as a reference of index position
    alphabet = list(map(chr, range(97, 123)))
    result = 0
    
    # If the matrix has only one 1 row then 0
    if len(arr) == 1:
        False
    else:
        # Iterating through the list and the lists within
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                # A catch to stop before the index goes beyond the length of the array
                if j == len(arr[i])-1:
                    break
                else:
                    # If the index[x] in list[1,2,... n] is greater in the alphabet
                    if alphabet.index(arr[j][i]) > alphabet.index(arr[j-2][i]):
                        # Result + 1
                        result = result + 1
                        break
    print(result)
    return result
    
numOrdered(test)
numOrdered(test2)
numOrdered(test3)
numOrdered(test4)
