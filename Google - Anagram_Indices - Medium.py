#Given a word w and a string s, find all indices in s which are the starting
#locations of anagrams of w. For example, given w is ab and s is abxaba,
#return [0,3,4].

from collections import defaultdict

def anagram_index(word : str, string : str):
    array = []
    count = 0
    for i in range(len(string)):
        for x in string[i:i + len(word)]:
            if x in word: 
                count += 1
        if count == len(word):
            array.append(i)
        count = 0
    return array

#passed, returned [0,3,4]
test_string = 'abxaba'

test_word = 'ab'

print(anagram_index(test_word, test_string))

#failed, returned [0,4,5,8,9,10,11] but should have returned [0,4,8,9,11] due to 
#repeating letters
test_string = 'ubhoubbhubuub'

test_word = 'ub'

print(anagram_index(test_word, test_string))

def anagram_index_v2(word : str, string : str):
    array = []
    freq = defaultdict(int)
    for i in word:
        freq[i] += 1
    
    for i in string[:len(word)]:
        freq[i] -= 1
        if freq[i] == 0:
            del freq[i]
    
    if not freq:
        array.append(0)
        
    for i in range(len(word), len(string)):
        start, end = string[i - len(word)], string[i]
        freq[start] += 1
        if freq[start] == 0:
            del freq[start]
        freq[end] += 1
        if freq[end] == 0:
            del freq[end]
        if not freq:
            start_index = i - len(word) + 1
            array.append(start_index)
    return array 

#passed, returned [0,3,4]
test_string = 'abxaba'

test_word = 'ab'

print(anagram_index_v2(test_word, test_string))

#failed, returned [0,4,5,8,9,10,11] but should have returned [0,4,8,9,11] due to 
#repeating letters
test_string = 'ubhoubbhubuub'

test_word = 'ub'

print(anagram_index_v2(test_word, test_string))