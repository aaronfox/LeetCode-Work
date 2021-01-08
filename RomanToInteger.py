# URL: https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        # Much shorter solution than if loop bonanza that is still intuitive: if a smaller value char
        # occurs before a larger value char, then subtract it instead of adding it
        conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        if len(s) == 1:
            return conv[s[0]]
        
        value = conv[s[len(s) - 1]]
        
        i = len(s) - 2
        
        while i > -1:
            if conv[s[i]] < conv[s[i + 1]]:
                value = value - conv[s[i]]
            else:
                value = value + conv[s[i]]
            i = i -1
        
        return value
        
        
        
        # Simplest, most straight forward solution in O(n) time and O(1) space
        prev_char = ''
        value = 0
        for char in s:
            if char == 'I':
                prev_char = 'I'
                value = value + 1
            elif char == 'V':
                if prev_char == 'I':
                    value = value - 2 + 5
                else:
                    value = value + 5
                prev_char = 'V'
            elif char == 'X':
                if prev_char == 'I':
                    value = value - 2 + 10
                else:
                    value = value + 10
                prev_char = 'X'
            elif char == 'L':
                if prev_char == 'X':
                    value = value - 20 + 50
                else:
                    value = value + 50
                prev_char = 'L'
            elif char == 'C':
                if prev_char == 'X':
                    value = value - 20 + 100
                else:
                    value = value + 100
                prev_char = 'C'
            elif char == 'D':
                if prev_char == 'C':
                    value = value - 200 + 500
                else:
                    value = value + 500
                prev_char = 'D'
            elif char == 'M':
                if prev_char == 'C':
                    value = value - 200 + 1000
                else:
                    value = value + 1000
                prev_char = 'M'
            else:
                return -1
                    
        return value
                