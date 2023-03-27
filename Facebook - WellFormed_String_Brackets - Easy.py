# This problem was asked by Facebook.
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def balanced(string : str):
    lst = []
    for char in string:
        #adding all possible opening brackets to a list
        if char in ["(", "[", "{"]:
            lst.append(char)
        else: 
            #if list is empty returning False
            if not lst:
                return False
            #if the subsequent closing bracket after the last iterated opening bracket doesn't equal the closing bracket returning False
            if (char == ")" and lst[-1] != "(") or \
                (char == "]" and lst[-1] != "[") or \
                (char == "}" and lst[-1] != "{"):
                return False
            #removing the last iterated opening bracket as that has now been paired
            lst.pop()
    #any opening brackets remaining in the list have not been closed and so will return False, otherwise returns True
    return len(lst) == 0

#returns True
test = "([])[]({})"

print(balanced(test))

#returns False
test = "([)]"

print(balanced(test))

#returns False
test = "((()"

print(balanced(test))

