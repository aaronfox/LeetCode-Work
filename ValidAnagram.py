# URL: https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Remove letters iteratively and make sure string is empty
        # O(n) runtime complexity
        # O(1) space complexity
        for c in s:
            if c in t:
                t = t.replace(c,'',1)
            else:
                return False
        print(t)
        print(c)
        if len(t) == 0:
            return True
        return False
            
        # Count up letters in each string. If the dicts match, return true
        # O(n) time complexity
        # O(n) space complexity
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        t_dict = {}
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        if t_dict == s_dict:
            return True

        return False
