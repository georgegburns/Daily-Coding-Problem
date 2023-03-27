# This problem was asked by Microsoft.
# Suppose an arithmetic expression is given as a binary tree. 
# Each leaf is an integer and each internal Node is one of '+', '−', '∗', or '/'.
# Given the root to such a tree, write a function to evaluate it.
# For example, given the following tree:
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
            
def evaluateEquation(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.data)
    
    left = evaluateEquation(root.left)
    right = evaluateEquation(root.right)
    
    if root.data == "+":
        return left + right
    if root.data == "-":
        return left - right
    if root.data == "/":
        return left / right
    if root.data == "*":
        return left * right
        
root = Node('*')
root.left = Node('+')
root.left.left = Node('3')
root.left.right = Node('2')
root.right = Node('+')
root.right.left = Node('4')
root.right.right = Node('5')

print(evaluateEquation(root))