# URL: https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers from left and right and compare the chars at them,
        # making sure to check for non alpha characters
        # O(n) time complexity
        # O(1) space complexity
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
            
