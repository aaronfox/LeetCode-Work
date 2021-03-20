# URL: https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n) time complexity
        # O(n) space complexity
        res = ""
        words = s.split(" ")
        for i in range(len(words) - 1, -1, -1):
            if words[i] != "":
                if i != 0:
                    res += words[i].strip() + " "
                else:
                    res += words[i].strip() 
            
        return res.strip()
