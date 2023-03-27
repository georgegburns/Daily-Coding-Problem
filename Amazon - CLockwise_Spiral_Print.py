# This problem was asked by Amazon.
# Given a N by M matrix of numbers, 
# print out the matrix in a clockwise spiral.
# For example, given the following matrix:
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

matrix = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

def clockwisePrint(matrix : list):
    check = []
    while len(check) != range(0, len(matrix[0]) * len(matrix)):
        (x, y) = (0,0)
        print(matrix[x][y])

            
    
    
        
            
            
clockwisePrint(matrix)