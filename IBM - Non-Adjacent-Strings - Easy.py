# Given a string with repeated characters, 
# rearrange the string so that no two adjacent characters are the same.
# If this is not possible, return None.

# For example, given "aaabbc", you could return "ababac". Given "aaab", return None.

TEST1 = "aaabbc"
TEST2 = "aaab"

def noAdjacent(word : str):
    word = [x for x in word]
    new_string = word[0]
    word.pop(0)
    while len(word) != 0:
        for index,letter in enumerate(word):
            if letter == new_string[len(new_string)-1]:
                continue
            elif len(word) > 1 and len(set(word)) == 1:
                return None
            else:
                new_string += letter
                word.pop(index)     
    return new_string

print(noAdjacent(TEST1))

print(noAdjacent(TEST2))