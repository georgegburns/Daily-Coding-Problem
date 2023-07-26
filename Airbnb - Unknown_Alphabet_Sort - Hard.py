# You come across a dictionary of sorted words in a language you've never seen before.
# Write a program that returns the correct order of letters in this language.

# For example given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
# you should return ['x', 'z', 'w', 'y']

TEST = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']

def unknownAlphabet(sorted_words : list):
    sorted_alphabet = []
    letters = list(set(letter for word in sorted_words for letter in word))

    for index, word in enumerate(sorted_words):
        if index == 0 or index == len(sorted_words)-1:
            sorted_alphabet.append(word[0])
        else:
            for sub_index, letter in enumerate(word):
                if  index != len(sorted_words)-1 and len(sorted_words[index+1]) == len(word):
                    if sorted_words[index+1][sub_index] == letter:
                        continue
                    elif letter not in sorted_alphabet:
                        sorted_alphabet.append(letter)
                        sorted_alphabet.append(sorted_words[index+1][sub_index])
    for letter in letters:
        if letter not in sorted_alphabet:
            sorted_alphabet.append(letter)
    
    return sorted_alphabet

# Returns ['x', 'z', 'w', 'y'] PASS -- REQUIRES TESTING
print(unknownAlphabet(TEST))