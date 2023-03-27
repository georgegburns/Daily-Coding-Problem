# This problem was asked by Google.
# The edit distance between two strings refers to the minimum number of character insertions,
# deletions, and substitutions required to change one string to the other. 
# For example, the edit distance between “kitten” 
# and “sitting” is three: substitute the “k” for “s”, 
# substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them.

def editDistance(word1 : str, word2 : str):
    distance = 0
    x = word1
    y = word2
    # to work out which word is longer to iterate the correct length
    if len(word1) > len(word2):
        x = word2
        y = word1
    for i in range(len(x)):
        # if the letter at the same indices is present in both words, continue
        if x[i] == y[i]:
            continue
        # otherwise add 1 to distance
        else:
            distance += 1
    # add any extra letters to distance
    distance += len(y) - len(x) 
    return distance

# returns 3
test1 = 'kitten'
test2 = 'sitting'

print(editDistance(test1, test2))

# returns 3
test1 = 'sitting'
test2 = 'kitten'

print(editDistance(test1, test2))

