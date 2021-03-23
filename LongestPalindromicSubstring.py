# URL: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    
    def expandAroundCenter(self, s, left, right):
        # Take advantage of expanding around a center character
        # and keep going outward until the the characters don't match
        # Note: should check odd number of letter palindromes and
        # even number of letter palindromes
        # O(n^2) runtime complexity since expanding around center can take O(n) time as well
        # O(1) space complexity
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        
        return R - L - 1
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Avoiding DP, expand around center for every index
        if len(s) <= 1:
            return s
        
        start = 0
        end = 0
        for i in range(len(s)):
            # For finding odd length palindromes like aba
            len1 = self.expandAroundCenter(s, i, i)
            # For finding even length palindromes like abba
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            length = max(len1, len2)
            
            # If a larger length is found,
            # keep track of its respective start and end indices
            # by setting start to the current index minus half the length
            # and by setting end index to current index plus half the length
            if length > end - start:
                start = i - int((length - 1) / 2)
                end = i + int(length / 2)
                
        return s[start:end + 1]
        
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
        
                

        
