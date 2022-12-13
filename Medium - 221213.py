# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def contained_in(s : str, st : set):
    s_list = []
    for i in st:
        if s in i[:2]:
            s_list.append(i)
    return s_list
            
        
        
#test
s = "st"

st = set(['sting', 'stripe', 'shin'])

print(contained_in(s, st))

s = "s"

st = set(['sting', 'stripe', 'shin'])

print(contained_in(s, st))

s = "sh"

st = set(['sting', 'stripe', 'shin'])

print(contained_in(s, st))