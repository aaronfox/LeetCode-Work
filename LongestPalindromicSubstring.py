# URL: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Dynamic Programming Solutions
        # Runs in O(n^2) time with O(n^2) space complexity to hold DP table
        if len(s) <= 1:
            return s
        
        # Solution using Dynamic Programming
        # dp[i][j] = 1 if substring Si to Sj is palindrome
        # dp[i][j] = 0 if substring Si to Sj is not palindrome
        
        # Palindromes of length 1
        # dp[i,i] = 1
        # Palindromes of length 2
        # dp[i][i+1] = 1 if Si == S(i+1)
        
        # Therefore
        # dp[i][j] = dp[i+1][j-1] && (Si == Sj)
        
        maxLength = 1
        start = 0
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]

        # All substrings of length 1 are palindromes
        for i in range(len(s)):
            dp[i][i] = True
        
        # print(dp)

        # Check substrings of length 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                maxLength = 2
                start = i
            
        # print(dp)

        # Check for all substrings of length of s
        for i in range(3, len(s) + 1):
            for j in range(len(s) - i + 1): # - i to exclude letters before starting index in prev for loop
                end = i + j - 1
                
                if dp[j + 1][end - 1] and s[j] == s[end]:
                    dp[j][end] = True
                    
                    if i > maxLength:
                        start = j
                        maxLength = i
                        
        # print(dp)
        return s[start:start + maxLength]               
        
                

        
