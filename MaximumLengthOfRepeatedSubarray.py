# URL: https://leetcode.com/problems/maximum-length-of-repeated-subarray
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # If A[i] == B[j]: dp[i][j] = dp[i+1][j+1] + 1
        # Invariant: answer for dp where i and j are larger is always calculated correctly  
        # Dynamic programming approach
        # O(n*m) runtime where n and m are the lengths of the arrays 
        # O(n*m) space complexity to store numbers in dp       

        # Can find max solution while passing through dp
        max = 0
        # Create empty table
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    if dp[i][j] > max:
                        max = dp[i][j]
        
        return max
        # # Answer is largest value in table
        # max = 0
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         if dp[i][j] > max:
        #             max = dp[i][j]
        # return max
