# URL: https://leetcode.com/discuss/interview-question/351783/
def isShuffledPalindrome(string):
    # let first index be count of a's in string, second index be count of b's in string, etc.
    letterOccurences = [0] * 26

    # Basically, a string is a shuffled palindrome if it has
    # one or none number of odd letter counts of strings
    for c in string.lower():
        letterOccurences[ord(c) - 97] += 1

    oddCountsOfLetters = 0
    for i in range(len(letterOccurences)):
        if letterOccurences[i] % 2 != 0:
            oddCountsOfLetters += 1
    
    return oddCountsOfLetters <= 1

def getNumSwaps(string):
    if string is None or len(string) == 0:
        return -1
    numSwaps = 0

    # Make sure string is a shuffled palindrome first
    if isShuffledPalindrome(string):
        # Have pointers at start and end and iterate across string
        # If chars at both pointers are same, then increment p1 and decrement p2
        # Otherwise, find matching pair and swap char to p2 index and inc swap count and shrink window
        # If no matching pair then swap once with adjacent index and increase swap count w/o shrinking window
        # Lastly, return swap count
        p1 = 0
        p2 = len(string) - 1

        # make char of string input
        string = list(string)

        while p2 > p1:
            if string[p1] == string[p2]:
                p1 += 1
                p2 -= 1
            else:
                temp = p2
                while temp > p1 and string[temp] != string[p1]:
                    temp -= 1
                
                # No match found, so single char. Swap adjacent chars
                if temp == p1:
                    temp_char = string[p1]
                    string[p1] = string[p1 + 1]
                    string[p1 + 1] = temp_char
                    numSwaps += 1
                # Else match was found and swap those until temp equals p2
                else:
                    while temp < p2:
                        temp_char = string[temp]
                        string[temp] = string[temp + 1]
                        string[temp + 1] = temp_char
                        temp += 1
                        numSwaps += 1
                    p1 += 1
                    p2 -= 1
        return numSwaps
    # If not a shuffled alindrome, return -1
    return -1
    

if __name__ == "__main__":
    print(getNumSwaps("mamad") == 3)
    print(getNumSwaps("asflkj") == -1)
    print(getNumSwaps("aabb") == 2)
    print(getNumSwaps("ntiin") == 1)
