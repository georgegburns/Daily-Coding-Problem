# Given a string, return whether it represents a number. Here are the different kinds of numbers:
# •	"10", a positive integer
# •	"-10", a negative integer
# •	"10.1", a positive real number
# •	"-10.1", a negative real number
# •	"1e5", a number in scientific notation
# And here are examples of non-numbers:
# •	"a"
# •	"x 1"
# •	"a -2"
# •	"-"

def numCheck(string : str):
    print(string)
    char = [x for x in string]
    ints = list(range(0, 10))
    nums = []
    e = char.count('e')
    dec = char.count('.')
    neg = char.count('-')
    for y in char:
        try:
            y = int(y)
            nums.append(y)
        except:
            continue
    try: 
        pos =  char.index('e')
    except:
        pos = 0
    try:
        first = int(char[0])
    except:
        first = char[0]
    if first == '-' or first in ints:
        if len(nums) > 0 and e <= 1 and dec <= 1 and neg <= 1 and pos <= 2:
            check = True
        else:
            check = False
    else:
        check = False
        
    return check

# Returns True PASS
test = "-10"
print(numCheck(test))

# Returns True PASS
test = "10"
print(numCheck(test))

# Returns True PASS
test = "10.1"
print(numCheck(test))

# Returns True PASS
test = "-10.1"
print(numCheck(test))

# Returns True PASS
test = "1e5"
print(numCheck(test))

# Returns False PASS
test = "a -2"
print(numCheck(test))

# Returns False PASS
test = "a"
print(numCheck(test))

# Returns False PASS
test = "x 1"
print(numCheck(test))

# Returns False PASS
test = "a -2"
print(numCheck(test))

# Returns False PASS
test = "-"
print(numCheck(test))