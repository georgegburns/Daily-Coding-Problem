# Given a string and a pattern, 
# find the starting indices of all occurrences of the pattern in the string.
# For example, given the string "abracadabra" and the pattern "abr", 
# you should return [0, 7].

TEST = 'abracadabra'

PATTERN = 'abr'

def substringString(string : str, substr: str):
    #breaking string into a list to iterate through
    string = [char for char in string]
    pattern = [char for char in substr]
    #this is needed to calculate the size of the selection as it loops
    length = len(pattern)
    result = []
    #looping through the string but subtracting the length-1 so as to not cause an index error
    for i in range(len(string)-(length-1)):
        #if the substring equals the 3 characters from an index then it will append the first index point to the result
        if pattern == string[i:i+length]:
            result.append(i)
    return result
            
#returns [0,7] PASS
print(substringString(TEST, PATTERN))