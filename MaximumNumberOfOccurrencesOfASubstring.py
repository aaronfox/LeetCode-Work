# URL: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Runtime: O(n) time complexity and O(n) space complexity for hashmap and sets
        # Note: maxSize is irrelevant here since minSize will always have a larger or equal freqencu of larger sizes
        # Find maximum number of occurrences of a substring
        hashMap = {}
        
        maxOcc = 0
        # For loop using sliding window approach runs in O(n)
        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            
            curr_set = []
            # Effectively O(1) since substring is <= minSize
            # Could also use Python's set here to make sure all values are unique
            for c in substring:
                if c not in curr_set:
                    curr_set.append(c)
            # Make sure too many unique letters aren't used
            if len(curr_set) <= maxLetters:
                if substring not in hashMap:
                    hashMap[substring] = 1
                else:
                    hashMap[substring] =  hashMap[substring] + 1
                maxOcc = max(maxOcc, hashMap[substring])
                
        return maxOcc
        
