# This problem was asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

def encoder(string : str):
    encoded = ''
    temp = []
    #iterating through the string
    for i in range(len(string)):
        # if the character is in the list already or the list is empty (False) appending the character to the list
        if string[i] in temp or not temp:
            temp.append(string[i])
        else:
            # once a new character is detected the length of the list is the first number and any index of the list is the second letter
            encoded += str(len(temp))
            encoded += temp[0]
            # clearing the list to iterate through again
            temp = []
            temp.append(string[i])
    # this picks up the [-1] index of the string
    encoded += str(len(temp))
    encoded += temp[0]
    return encoded

def decoder(string : str):
    decoded = ''
    temp = []
    # iterating through the encoded string and pulling out all of the letters (every 2 index from 1)
    for j in range(1, len(string), 2):
        temp.append(string[j])
    # iterating through the encoded string and pulling out the quantity of the letters (every 2 index from 0)
    for i in range(0, len(string), 2):
        count = 0
        # creating a counter to loop the number of times of the quantity and adding the corresponding letter to the decoded string
        while count < int(string[i]):
            decoded += temp[0]
            count += 1
        # removing the first index of the temp so that the next relevant letter is in the correct index
        temp.pop(0)     
    return decoded
        
# returns 4A3B2C1D2A
test = "AAAABBBCCDAA"

print(encoder(test))

# returns AAAABBBCCDAA
print(decoder(encoder(test)))
        
