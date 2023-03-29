# This problem was asked by Google.
# Given a string of words delimited by spaces, reverse the words in string. 
# For example, given "hello world here", return "here world hello"

string = "hello world here"

def reverseWords(string: str):
    return " ".join(reversed(string.split(" ")))
        
print(reverseWords(string))