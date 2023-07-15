# Spreadsheets often use this alphabetical encoding for its columns: 
# "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

# Given a column number, return its alphabetical column id. 
# For example, given 1, return "A". Given 27, return "AA".

from string import ascii_uppercase as alp

TEST1 = 'A' #= 1
TEST2 = 'AA' #= 27
TEST3 = 'BA' #= 53
TEST4 = 'AAA' #= 703
TEST5 = 'XFD' #= 16384

def alphabetDecoder(string : str):
    #dictionary of alphabet : numerical number using string.ascii
    alphabet = {}
    for i, char in enumerate(alp):
        alphabet[char] = i + 1
    result = 0
    #to ensure input is in uppercase
    string = string.upper()
    length = len(string)-1
    
    # ea cycle of letters results in the numerical value of the letter times 26 to the power of the length-1
    # i.e. A is 1 (1 * 26 ** 1-1 (0) = 1), 
    # AA is 27, 1 (from the previous calc) + (1 * 26 ** 2-1 (1) /LEN(AA)=2)/ = 26), etc...
    for letter in string:
        result += alphabet[letter] * 26 ** length
        length -= 1 
    return result

#returns 1 PASS
print(alphabetDecoder(TEST1))

#returns 27 PASS
print(alphabetDecoder(TEST2))

#returns 78 PASS
print(alphabetDecoder(TEST3))

#returns 703 PASS
print(alphabetDecoder(TEST4))

#returns 16384 PASS
print(alphabetDecoder(TEST5))

TESTA = 1
TESTAA = 27
TESTAAA = 703
TESTBA = 53
TESTXFD = 16384

def alphabetEncoder(num : int):
    result = ''
    #dictionary of alphabet : numerical number using string.ascii
    alphabet = {}
    for i, char in enumerate(alp):
        alphabet[i+1] = char
    
    # ea individual letter value is the modulus (leftover) of the num / 26
    # ea subsequent cycle must then subtract the modulus, 
    # then divide by 26 to get the new number
    # ea letter is produced from the end so for XFD, D is found first
    # the loop ends when the num = 0
    while num != 0:
        letter = num % 26
        result = alphabet[letter] + result
        num = (num - letter) / 26
    return result

#returns A PASS
print(alphabetEncoder(TESTA))

#returns AA PASS
print(alphabetEncoder(TESTAA))

#returns AAA PASS
print(alphabetEncoder(TESTAAA))

#returns BA PASS
print(alphabetEncoder(TESTBA))

#returns XFD PASS
print(alphabetEncoder(TESTXFD))
    

