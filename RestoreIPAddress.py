# URL: https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    # O(3^n) time complexity
    # O(3^n) space complexity
    def __init__(self):
        self.output = []
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.helper(s, [])
        return self.output
    
    def helper(self, candidates, selected):
        # Generate combinations of numbers by slicing candidates with 1 digit, 2 digits, and 3 digits from left
        # Check if slice is within correct range (e.g. for length 2 make sure its 10 <= x <= 99)
        # Base case is when there are no candidates to slice and there are 4 slices
        if len(candidates) == 0 and len(selected) == 4:
            # Found correct IP!
            ip = '.'.join(selected)
            self.output.append(ip)
        if len(selected) > 4:
            # Can't have IP with more than 4 segments
            return
        if len(candidates) > 0:
            # If we have at least one candidate, call helper with remaining candidates
            a = candidates[0]
            remain = candidates[1:]
            self.helper(remain, selected + [a])
        if len(candidates) > 1:
            a = candidates[:2]
            # Make sure a is between 10 and 99
            if int(a) >= 10 and int(a) <= 99:
                remain = candidates[2:]
                self.helper(remain, selected + [a])
        if len(candidates) > 2:
            a = candidates[:3]
            if int(a) >= 100 and int(a) <= 255:
                remain = candidates[3:]
                self.helper(remain, selected + [a])
                
                
        
    
