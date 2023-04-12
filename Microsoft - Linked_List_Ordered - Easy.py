# Let's represent an integer in a linked list format by having each node represent a digit in the number. 
# The nodes make up the number in reversed order.
# For example, the following linked list:
# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.
# Given two linked lists in this format, return their sum in the same linked list format.
# For example, given
# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:
# 4 -> 2 -> 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
class LinkedList():
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
TEST = 25
TEST2 = 99

def nodeBuilder(llist, num : int):
    current_node = False
    for i in reversed(str(num)):
        if current_node == False:
            current_node = Node(i)
            llist.head = current_node
        else:
            previous_node = current_node
            current_node = Node(i)
            previous_node.next = current_node
    return llist

TESTLIST = LinkedList()
TESTLIST2 = LinkedList()

nodeBuilder(TESTLIST, TEST)
nodeBuilder(TESTLIST2, TEST2)

def sumLinkedLists(llist1, llist2):
    result = LinkedList()
    num1 = ''
    num2 = ''
    for node in llist1:
        num1 += str(node)
    for node in llist2:
        num2 += str(node)
    num1 = int(num1[::-1])
    num2 = int(num2[::-1])
    num3 = num1 + num2
    nodeBuilder(result, num3)
    return result

print(sumLinkedLists(TESTLIST, TESTLIST2))