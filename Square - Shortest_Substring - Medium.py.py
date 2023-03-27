# This problem was asked by Square.
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.
# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
# If there is no substring containing all the characters in the set, return null.

string = 'figehaeci'
lst = {'a', 'e', 'i'}

def shortestSubstring(word : str, lst : set):
    sub = ''
    result = None
    size2 = 0
    for i, char in enumerate(word):
        for j, char2 in enumerate(word[i+1:]):
            if char in lst and char not in sub:
                sub += char
            if char2 in lst and char2 not in sub:
                sub += char2
        if len(sub) == len(lst):
            size1 = j - i
            if i == 0:
                size2 = size1
                sub = ''
                continue
            if size1 < size2:
                size2 = size1
                result = word[i:i+word[i:].index(sub[-1])+1]
                sub = ''
    print(result)
    return result

shortestSubstring(string, lst)