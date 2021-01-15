# URL: https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming approach
        # O(n) runtime complexity
        # O(n) space complexity
        if s[0] == "0":
            return 0
        
        # Dynamic Programming table to keep track of 
        dp = [0] * (len(s) + 1)
        # Let there be one way to decode empty string for DP purposes
        dp[0] = 1
        # There is either one (or no) way to decode string of size 1
        if s[0] != 0:
            dp[1] = 1
        else:
            dp[1] = 0

        print(dp)
        for i in range(2, len(s) + 1):
            oneDigit = int(s[i - 1])
            twoDigit = int(s[i - 2:i])
            
            if oneDigit > 0 and oneDigit < 10:
                dp[i] += dp[i - 1]

            if twoDigit > 9 and twoDigit < 27:
                dp[i] += dp[i - 2]

        return dp[len(s)]
                
