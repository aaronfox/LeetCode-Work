# URL: https://leetcode.com/problems/reverse-words-in-a-string-ii/
class Solution:
    # Here, first reverse whole array
    # Then iterate through array and reverse each individual word using same function
    # Don't forget about last word as well
    # Reverse array using two pointers and swapping them
    # O(n) runtime complexity for two passes on string
    # O(1) space complexity since reversing is done in place
    def reverseArray(self, s, p1, p2):
        p1 = p1
        p2 = p2
        
        while p1 < p2:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            p1 += 1
            p2 -= 1
        return
    
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Can simply reverse the whole array and then reverse each word
        self.reverseArray(s, 0, len(s) - 1)
        
        # Then reverse each word
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            if s[i] == ' ':
                p2 = i - 1
                self.reverseArray(s, p1, p2)
                p1 = i + 1
        
        # Reverse last word as well
        self.reverseArray(s, p1, len(s) - 1)
