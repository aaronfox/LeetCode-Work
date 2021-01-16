# URL: https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Simple for loop solution comparing first word with all other words
        # O(l*n) runtime complexity where l is the length of the string and n is the number of strings
        # O(l) space complexity because that depends on length of string but is effectively O(1) 
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        possible_prefix = strs[0]
        answer = ""
        max_length = math.inf
        
        for i in range(1, len(strs)):
            str = strs[i]
            left = ""

            if len(possible_prefix) >= len(str):
                for i in range(len(str)):
                    if possible_prefix[i] == str[i]:
                        left += str[i]
                    else:
                        break
            else:
                for i in range(len(possible_prefix)):
                    if possible_prefix[i] == str[i]:
                        left += str[i]
                    else:
                        break
            
            if len(left) < max_length:
                answer = left
                max_length = len(left)
                    
        return answer
                
                    
                
