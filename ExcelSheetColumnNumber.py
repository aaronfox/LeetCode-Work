# URL: https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # The logic here is that each letter represents a number value worth
        # 1 (A) to 26 (Z)
        # Similar to hex numbers, the value of each place is worth
        # 26 raised to the power of the number of indices it is away from the right
        # e.g. BA = (2 * 26^1) + (1 * 26^0)
        # and CBA = (3 * 26^2) + (2 * 26^1) + (1 * 26^0)
        # O(n) time complexity where n is the length of columnTitle
        # O(1) space complexity
        n = len(columnTitle)
        res = 0
        for i in range(len(columnTitle)):
            letter = columnTitle[i]
            letterVal = ord(letter) - ord('A') + 1 # subtract 64 from each number since A as value 1
            res += letterVal * (26 ** (n - i - 1))
            
        return res
