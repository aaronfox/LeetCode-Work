# LCS Practice Using dynamic Programming
# Runs in O(m*n) time complexity and O(m*n) space complexity for the dp matrix,
# where m and n represent the lengths of the strings
# LCS: Find longest common substring from two given strings
# Can use this with dynamic programming (bottom-up approach) like so:
#     C O W L O
#   0 0 0 0 0 0
# H 0 0 0 0 0 0
# O 0 0 1 0 0 1
# W 0 0 0 2 0 0
# L 0 0 0 0 3 0
# S 0 0 0 0 0 0
# Basically, the rule is:
# If string1[i] == string2[j]: dp[i][j] = dp[i-1][j-1] + 1
# Else: dp[i][j] = 0

def LCS(s1, s2):
    dp = [[0] * (len(s1) + 1)] * (len(s2) + 1)
    max = 0
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max:
                    max = dp[i][j]
    
    print('Max is ' + str(max))
    return max
                
# Sample Test Cases
s1 = 'ABC'
s1 = 'COWLOX'

s2 = 'AB'
s2 = 'HOWLS'

LCS(s1, s2)
