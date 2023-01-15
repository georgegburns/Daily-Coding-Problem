# This problem was asked by Amazon.

# Implement a stack that has the following methods:
# •	push(val), which pushes an element onto the stack
# •	pop(), which pops off and returns the topmost element of the stack. 
# If there are no elements in the stack, then it should throw an error or return null.
# •	max(), which returns the maximum value in the stack currently. 
# If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Stack:
    def __init__(self, *items):
        self.items = []
        for item in items:
            self.items.append(item)
        
    def push(self, new):
        self.items.append(new)
        
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def max(self):
        if len(self.items) == 0:
            return None
        return max(self.items)
      
item1 = 1
item2 = 2
item3 = 3
item4 = 4
item5 = 5

some = Stack(item1, item2, item3, item4)
none = Stack()

# returns [1,2,3,4]
print(some.items)

# adds item5 to the end
some.push(item5)
print(some.items)

# removes index[0] item and returns it else prints None
print(some.pop())
print(none.pop())
print(some.items)

# returns the maximum value else returns None
print(some.max())
print(none.max())
