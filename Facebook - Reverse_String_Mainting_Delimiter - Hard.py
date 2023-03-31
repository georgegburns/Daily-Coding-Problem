# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. 
# For example, given "hello/world:here", return "here/world:hello"
# Follow-up: Does your solution work for the following cases: 
# "hello/world:here/", "hello//world:here"
import string

def stringReverseDelimiter(text : str):
    """
        Variables
    
    """
    # This is used to establish whether a character is a letter or a delimiter
    LETTERS = string.ascii_letters
    SEPERATE = []
    TEMP = []
    
    """

        Main function

    """
    
    # Iterating through each character in the string and assigning to a list depending on whether it is a letter or a non-letter
    for i in range(len(text)):
        if not TEMP:
            TEMP.append(text[i])
        elif text[i] not in LETTERS and TEMP[-1] in LETTERS:
            SEPERATE.append("".join(TEMP))
            TEMP = []
            TEMP.append(text[i])
        elif text[i] in LETTERS and TEMP[-1] not in LETTERS:
            SEPERATE.append("".join(TEMP))
            TEMP = []
            TEMP.append(text[i])
        else:
            TEMP.append(text[i])
    # These capture the last stored variables after the loop has ended   
    SEPERATE.append("".join(TEMP))
    
    # Seperating out into two lists one of words and the other of delimiters
    WORDS = [x for x in SEPERATE if x[0] in LETTERS]
    DELIMITERS = [x for x in SEPERATE if x[0] not in LETTERS]
    
    # Reversing the list of words
    WORDS.reverse()
    
    RESULTS = []
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
#TEST = 'hello/world:here'

# Produces here/world:hello/ PASS
#TEST = "hello/world:here/"

# Produces here//world:hello PASS
TEST = "hello//world:here"

print(stringReverseDelimiter(TEST))