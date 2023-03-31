# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. 
# For example, given "hello/world:here", return "here/world:hello"
# Follow-up: Does your solution work for the following cases: 
# "hello/world:here/", "hello//world:here"
import string
import re

def stringReverseDelimiter(text : str):
    """
        Variables
    
    """
    # This is used to establish whether a character is a letter or a delimiter
    LETTERS = string.ascii_letters
    RESULTS = []
    WORDS = re.split('\W', text)
    DELIMITERS = re.split('[a-zA-Z]', text)
    WORDS = [x for x in WORDS if x]
    DELIMITERS = [x for x in DELIMITERS if x]
    
    """

        Main function

    """
    # Reversing the list of words
    WORDS.reverse()

    # This is here to ensure that all the words / delimiters are captured in circumstances where they aren't even
    COUNT = max(len(WORDS), len(DELIMITERS))
    
    # This then creates a new list placing either a word/delimiter first depending on the original string
    for i in range(COUNT):
        try:
            WORD = WORDS[i]
        except:
            WORD = ""
        try:
            DELIMITER = DELIMITERS[i]
        except:
            DELIMITER = ""
        if text[0] in LETTERS:
            RESULTS.append(WORD + DELIMITER)
        else:
            RESULTS.append(DELIMITER+WORD)

    # Joining the new list to produce the result
    RESULT = "".join(RESULTS).strip()
    return RESULT

# Produces here/world:hello PASS 
TEST = 'hello/world:here'

# Produces here/world:hello/ PASS
#TEST = "hello/world:here/"

# Produces here//world:hello PASS
#TEST = "hello//world:here"

print(stringReverseDelimiter(TEST))