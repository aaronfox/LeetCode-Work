# URL: https://leetcode.com/problems/implement-strstr
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # A less cheaty way of not using built in functions
        # O(n) runtime complexity
        # O(1) space complexity
        if len(needle) == 0 or haystack == needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
    
        # Can use a try-except block with built-in index function
        # index() returns ValueError so need try-except block if 
        # not found
        # O(1) time compelexity
        # O(1) space complexity
        try:
            return haystack.index(needle)
        except:
            return -1;
