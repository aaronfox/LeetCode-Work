# URL: https://leetcode.com/problems/unique-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use dynamic programming to store number of unique paths to get to each square
        # O(m *n) time complexity
        # O(m * n) space complexity for storing array
        # TODO: Can optimize space complexity to just use one row
        dp = [[0 for i in range(n)] for j in range(m)]
        print(dp)
        # Top row and leftmost column only have one unique path to reach them
        for i in range(m):
            dp[i][0] = 1
            
        for j in range(n):
            dp[0][j] = 1
            
        # In this dp, it can be seen that the number of possible unique paths 
        # is the sum of the number of unique paths from the block above and
        # the number of unique paths from the block to the left of the current block
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j-1]
        return dp[m-1][n-1]
