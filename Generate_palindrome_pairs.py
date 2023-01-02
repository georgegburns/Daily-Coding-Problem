# Given a list of words, find all pairs of unique indices
# such that the concatenation of the two words is a palindrome.
# For example, given the list ['code','edoc','da','d'], return [(0,1), (1,0), (2,3)]

def palindromes(lst : list):
    results = []
    # a function to check if a word(s) are palindromes
    def is_palindrome(word : str):
        return word == word[::-1]
    #iterating through the list of words twice
    for i, word1 in enumerate(lst):
        for j, word2 in enumerate(lst):
            #comparing if the index matches
            if i == j:
                continue
            #if the index doesn't checking if they are a palindrome in combination
            if is_palindrome(word1 + word2):
                results.append((i, j))
    return results

#produces [(0,1), (1,0), (2,3)]
test = ['code','edoc','da','d']

print(palindromes(test))