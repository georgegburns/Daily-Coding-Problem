# This problem was asked by Google.

# A unival tree (which stands for "universal value") 
# is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
test = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

count = 0

def count_trees(node, count):
    value = node.value
    print(node.value)
    if node.left != None:
        if node.value == node.left.value:
            print(node.value == node.left.value)
            count += 1
            if node.left != None:
                count_trees(node.left, count)
    if node.right != None:
        if node.value == node.right.value:
            print(node.value == node.right.value)
            count += 1
            if node.right != None:
                count_trees(node.right, count)
    return count

print(count_trees(test, count))