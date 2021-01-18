# URL: https://leetcode.com/problems/zigzag-conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Create array of empty strings that will be changed later
        # O(l*n) runtime complexity, where l is the length of the string and n s the number of rows
        # O(l * n) space complexity
        arr = [""] * numRows
        
        i = 0
        while i < len(s):
            # Going down
            for ix in range(0, numRows):
                if i < len(s):
                    arr[ix] = arr[ix] + s[i]
                    i += 1
            # Going diagonally up
            for ix in range(numRows - 2, 0, -1):
                if  i < len(s):
                    arr[ix] = arr[ix] + s[i]
                    i += 1
                    
        # Return array of strings
        res = ""
        for i in range(len(arr)):
            res += arr[i]
        
        return res
