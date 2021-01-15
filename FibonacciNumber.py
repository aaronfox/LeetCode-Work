# URL: https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        # Dynamic fib solution for fun
        # O(n) time complexity
        # O(n) space complexity
        if n == 0 or n == 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        if n == 0:
            return 0
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
