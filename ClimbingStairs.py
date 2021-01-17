# URL: https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        # Using DP, iteratively increment dp array for how many steps it takes to get to that step
        # Can see from this pattern that it's just prev two steps added together
        # 1: 1
        # 2: 2
        # 3: 3
        # 4: 5
        # 5: 8
        # O(n) runtime complexity
        # O(n) space complexity
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
