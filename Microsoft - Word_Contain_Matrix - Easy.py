# This problem was asked by Microsoft.
# Given a 2D matrix of characters 
# and a target word, 
# write a function that returns whether 
# the word can be found in the matrix 
# by going left-to-right, or up-to-down.
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', 
# you should return true, 
# since it's the leftmost column. 
# Similarly, given the target word 'MASS', 
# you should return true, since it's the last row.

matrix = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

def wordContain(matrix : list, word : str):
    comp = []
    for i in range(len(word)):
        comp.append(word[i])
    #checking horizontally
    for j in matrix: 
        if comp == j:
            return True
    #checking vertically
    for x in range(len(matrix)):
        col = []
        for y in matrix:
            col.append(y[x])
        if col == comp:
            return True
             
test = 'FOAM' 
      
print(wordContain(matrix, test))

test = 'MASS'
print(wordContain(matrix, test))
