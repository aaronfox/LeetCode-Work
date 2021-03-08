# URL: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
class Solution:
    def minDeletions(self, s: str) -> int:
        # First get count of every letter
        import collections
        count = collections.Counter(s)
        num_deletions = 0
        used_values = set()
        
        for char, freq in count.items():
            # Iterate over possible frequencies and delete char if needed
            while freq > 0 and freq in used_values:
                freq -= 1
                num_deletions += 1
            used_values.add(freq)
                
        return num_deletions
