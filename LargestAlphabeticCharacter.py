# URL: https://www.geeksforgeeks.org/find-the-largest-alphabetic-character-present-in-the-string/
# Find the largest Alphabetic character present in the string
# Given a string str, our task is to find the Largest Alphabetic Character,
# whose both uppercase and lowercase are present in the string. The uppercase
# character should be returned. If there is no such character then return -1
# otherwise print the uppercase letter of the character.

# Use list to keep track of letters
# Keep iterating through each letter.
# Check if opposite case is already in list.
# If so, check if its value is larger than other max vals and set max appropriately
def largestAlphabeticCharacter(string):
    max = -1
    letters = []
    for c in string:
        if c.islower() and c.upper() in letters or c.isupper() and c.lower() in letters:
            if ord(c.upper()) > max:
                max = ord(c)
        else:
            letters.append(c)

    if max == -1:
        return max
    return chr(max)

print(largestAlphabeticCharacter('admeDCAB'))
print(largestAlphabeticCharacter('admeDCAB') == 'D')
print(largestAlphabeticCharacter('dAeB'))
print(largestAlphabeticCharacter('dAeB') == -1)
