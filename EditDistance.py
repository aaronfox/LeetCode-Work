 # URL: https://leetcode.com/problems/edit-distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Use dynamic programming here with a 2D table that is m by n length
        # where n is length of word1 and m is length of word2
        # Basically, the algorithm here is
        # if word1[j] == word2[i]: dp[i][j] = dp[i-1][j-1]
        # elif word1[j] != word2[i]: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 
        # since we just need to add one to the minimum yielding prior operation
        # This works since dp[i][j-1] represents deleting a char to retrieve last char in word2
        # dp[i-1][j-1] represents replacing the char there from both word1 and word2
        # and dp[i-1][j] represents inserting a char from word1
        
        # Create empty dynamic programming array filled with 0s
        # Add one to length to add initializtion row and column
        dp = []
        for i in range(len(word2) + 1):
            arr = []
            for j in range(len(word1) + 1):
                arr.append(0)
            dp.append(arr)

        # Initialize first row to be i since it takes i operations for empty string to get to a string with i letters via insertions
        for i in range(len(word1) + 1):
            dp[0][i] = i
        
        # Initialize first column to be i since it takes i operations for empty string to get to a string with i letters via insertions
        for i in range(len(word2) + 1):
            dp[i][0] = i
        
        # Iterate through each row.
        # If letters are equal, its equal to the diagonal value as no values are changed
        # Else, its equal to the minimum value of inserting, deleting, or replacing + 1 since one change must be made
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete_val = dp[i][j - 1]
                    replace_val = dp[i - 1][j - 1]
                    insert_val = dp[i - 1][j]
                    dp[i][j] = min(delete_val, replace_val, insert_val) + 1
        
        # # Print out dp
        # for i in range(len(word2) + 1):
        #     print(dp[i])
        
        # Solution is found at bottom right corner of dp    
        return dp[len(word2)][len(word1)]

                       
