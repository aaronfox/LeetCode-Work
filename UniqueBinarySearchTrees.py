# URL: https://leetcode.com/problems/unique-binary-search-trees/
class Solution:
    def numTrees(self, n: int) -> int:
        # Use dynamic programming to calculate the number of unique BSTs
        # G(n) = number of unique BSTs for a sequence of length n
        # F(i,n) = number of unique BST where the number i is the root of BST (1 <= i <= n)
        # The answer we need is G(n)
        # G(n) = sum from 1 to n of F(i,n)
        # Assume G(0) = 1 and G(1) = 1 since there is one way to construct a BST of length 0 and 1
        # Generalized, F(i,n) = G(i-1) * G(n-1)
        # So, G(n) = sum from 1 to n of (G(i-1) * G(n-1))
        # O(n^2) time complexity for the number of iterations of the sum over all elements
        # O(n) space complexity for dp array
        dp = [0 for x in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += d`p[j - 1] * dp[i - j]
                
        return dp[n]
        
