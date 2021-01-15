# URL: https://leetcode.com/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # For both solutions:
        # O(n) runtime complexity
        # O(1) space complexity
        
        # Note: only upper and lower latin letters can be used
        # SOLUTION ONE: count num capital and lowercase letters
        num_lower = 0
        num_upper = 0
        for c in word:
            if ord(c) < 97:
                num_upper += 1
            else:
                num_lower += 1
        
        if num_lower == len(word) or num_upper == len(word):
            return True
        
        if num_upper == 1 and ord(word[0]) < 97:
            return True
        
        return False
        
        
        
        # SOLUTION TWO: Simple for loop with if checks
        firstCap = False
        if ord(word[0]) < 97:
            firstCap = True
        has_cap_after_first = None
        has_lower = None
        
        for i in range(1, len(word)):
            # If letter uppercase
            if ord(word[i]) < 97:
                # Then all other letters have to be upper too
                if firstCap == False:
                    return False
                if has_lower:
                    return False
                # Cannot have first capital and then lower and then capital
                if has_cap_after_first == False:
                    return False
                has_cap_after_first = True
            else:
                # If lower, make sure no other caps in word
                if has_cap_after_first:
                    return False
                has_lower = True
        return True
