# URL: https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        # O(n) runtime I believe, but it's complicated with the two while loops
        # O(n) space complexity as well to store the set, but not confident in that...
        curr_sum = 0
        memory_set = set()
        while curr_sum != 1:
            n = curr_sum
            curr_sum = 0
            while n != 0:
                curr_sum += (n % 10) ** 2
                n = int(n / 10)
            if curr_sum in memory_set:
                return False
            memory_set.add(curr_sum)

        
        return True
