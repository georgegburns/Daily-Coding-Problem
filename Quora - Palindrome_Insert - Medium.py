# This problem was asked by Quora.
# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
# If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). 
# There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".


def smallestPalindrome(word : str):
    matching = []
    palindrome = ""
    word = " " + word
    for i in range(1, len(word)):
        if word[i] == word[-i]:
            matching.append((i,-i))
    return matching

test = "google"

print(smallestPalindrome(test))

test = "race"

print(smallestPalindrome(test))