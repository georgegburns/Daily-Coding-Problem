# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node):
    val = node.val
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    if node.right:
        right = serialize(node.right)
    else:
        right = None
    serialized = [val, left, right]
    return serialized

print(serialize(node))

def deserialize(serial_node):
    deserialized = serial_node.split("/")
    for i in deserialized:
        root = i[0]
        
    
    return deserialized
    
print(deserialize(serialize(node)))

test


# assert deserialize(serialize(node)).left.left.val == 'left.left'