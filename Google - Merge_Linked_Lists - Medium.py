# This problem was asked by Google.

# Given k sorted singly linked lists, 
# write a function to merge all the lists 
# into one sorted singly linked list.

class ListNode():
    def __init__(self, val=None,next=None):
        self.val = val
        self.next = next
        
def printList(head):
    temp = head
    while temp:
        print(temp.val, end = " ")
        temp = temp.next

data = [[2,1],[4,3]]
head = None
sorted_list = []

for i in range(len(data)):
    for j in data[i]:
        head = ListNode(j, head)
printList(head)
