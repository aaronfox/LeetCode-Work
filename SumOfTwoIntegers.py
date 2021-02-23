# URL: https://leetcode.com/problems/sum-of-two-integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Not gonna lie, I need to understand this bit manipulation a little more
        # O(n) time complexity where n is the size of b
        # O(1) space complexity
        if a == 0:
            return b
        elif b == 0:
            return a
        
        mask = 0xffffffff
        c = 0
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    
        # If a is negative
        if (a >> 31) & 1:
            return ~(a ^ mask)
        return a
