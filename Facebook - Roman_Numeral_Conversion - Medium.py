# Given a number in Roman numeral format, convert it to decimal.

# The values of Roman numerals are as follows:

# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation 
# for numbers such as IV and XL.

# For the input XIV, for instance, you should return 14.


def romanConverter(roman : str):
    ROMAN =  {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    convert = 0
    skip = False
    for index, char in enumerate(roman):
        #a catch for non-roman numerals
        try: 
            ROMAN[char]
        except:
            convert = 'Invalid Roman Number'
            break
        #checking if the roman character starts with 1, 
        # that the index is not out of bounds, 
        # and that the following value is greater than the previous value
        if str(ROMAN[char])[0] == '1' and index != len(roman)-1 and ROMAN[roman[index+1]] == ROMAN[char]*5:
            #adding (the next value - the previous value) i.e. IV = 4
            convert += (ROMAN[roman[index+1]] - ROMAN[char])
            #setting skip to true so as to not readd the next value, 
            # this allows for IV to be 4 rather than 4+5
            skip = not skip
            continue
        elif skip == False:
            convert += ROMAN[char]
        skip = False
    return convert


TEST = 'CDXLIV'
TEST2 = 'DCLXVI'
TEST3 = 'XXX'
TEST4 = 'MMXXIII'
TEST5 = 'PP'

#returns 444 PASS
print(romanConverter(TEST))

#returns 666 PASS
print(romanConverter(TEST2))

#returns 30 PASS
print(romanConverter(TEST3))

#returns 2023 PASS
print(romanConverter(TEST4))

#returns Invalid Roman Number PASS
print(romanConverter(TEST5))